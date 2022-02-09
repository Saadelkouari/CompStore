from django.http.response import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render
from lxml import etree
import xml.etree.ElementTree as ET
from io import StringIO
import xmlschema
# Create your views here.
carts_schema=xmlschema.XMLSchema11(r'D:\ComputerStore\carts\database\carts.xsd')
cartv=r"D:\ComputerStore\carts\database\cartv.xml"
def connect_db(name):
    fcarts=open("D:\\ComputerStore\\"+name+"\\database\\"+name+".xml","r")
    carts=fcarts.read()
    fcarts.close()
    return etree.parse(StringIO(carts))
def validate(body):
    f=open(cartv,'w')
    body_unicode = body.decode('utf-8')
    f.write(body_unicode)
    f.close()
    try:
        carts_schema.validate(cartv)
        return True
    except Exception as e:
        print(e)
        return False

def getinput():
    f=open(cartv,'r')
    input=f.read()
    f.close()
    return etree.parse(StringIO(input))
def get_user_cart(userId):
    carts=connect_db('carts')
  
    if bool(carts.getroot().xpath("/carts/cart[@userId="+str(userId)+"]")):
        cartsv=etree.Element('carts')
        cartsv.append(carts.getroot().xpath("/carts/cart[@userId="+str(userId)+"]")[0])
        return cartsv[0]
    
    cart=etree.Element('cart')
    cart.set("userId",str(userId))
    total=etree.Element('total')
    cart.append(total)
    total.text='0'
    carts.getroot().append(cart)
    carts.write(r"D:\ComputerStore\carts\database\carts.xml")
    cartsv=etree.Element('carts')
    cartsv.append(cart)
    return cart
def get_computer(compId):
    computers=connect_db('computers')
    computer=computers.getroot().xpath("/computers/computer[@id="+str(compId)+"]")[0]
    return computer
def get_cart(request):
    if request.method =='POST':
        if validate(request.body) == False:
            return HttpResponseBadRequest("Invalid input")
        userId=getinput().getroot().get('userId')
        users=connect_db('users')
        if bool(users.getroot().xpath("/users/user[@id="+str(userId)+"]"))==False:
            return HttpResponseBadRequest("User Does Not Exist")
        cart=get_user_cart(userId)
        cart.getroottree().write(cartv)
        return HttpResponse(open(cartv).read(),content_type="application/xml")

def empty_cart(request):
    if request.method == 'POST':
        if validate(request.body) == False:
            return HttpResponseBadRequest("Invalid input")
        userId=getinput().getroot().get('userId')
        carts=connect_db('carts')
        if bool(carts.getroot().xpath("/carts/cart[@userId="+str(userId)+"]"))==False:
            return HttpResponseBadRequest("User Does Not Exist")
        cart=carts.getroot().xpath("/carts/cart[@userId="+str(userId)+"]")[0]
        for child in cart:
            if child.tag != 'total':
                cart.remove(child)
            if child.tag=='total':
                child.text='0'
        carts.write(r"D:\ComputerStore\carts\database\carts.xml")
        return HttpResponse("Cart emptied successfully")



def handle_add(request):
    carts_schema=xmlschema.XMLSchema11(r'D:\ComputerStore\carts\database\carts.xsd')
    if request.method == "POST":
        if validate(request.body) == False:
            return HttpResponseBadRequest("Invalid input")
        userId=getinput().getroot().get('userId')
        compId=getinput().getroot()[0].text
        users=connect_db('users')
        if bool(users.getroot().xpath("/users/user[@id="+str(userId)+"]"))==False:
            return HttpResponseBadRequest("User Does Not Exist")
        cart=get_user_cart(userId)
        if bool(cart.xpath('computer[@id='+str(compId)+']')):
            computer=cart.xpath('computer[@id='+str(compId)+']')[0]
            for elt in computer:
                if elt.tag=='qte':
                    elt.text=str(int(elt.text)+1)
                if elt.tag=='price':
                    price=float(elt.text)
                if elt.tag=='total':
                    total=elt
            total.text=str(float(total.text)+float(price))
            for elt in cart:
                if elt.tag=='total':
                    elt.text=str(float(elt.text)+price)
            cart.getroottree().write(cartv)
            carts_schema.validate(cartv)
            cart.getroottree().write(r"D:\ComputerStore\carts\database\carts.xml")
            carts_schema.validate(r"D:\ComputerStore\carts\database\carts.xml")
            return HttpResponse("Item incremented")
        computer=get_computer(compId)
        total=etree.Element('total')

        for spec in computer:
            if spec.tag not in ["manufacturer","series","model","image","price","qte","total"]:
                spec.getparent().remove(spec)
            if spec.tag=='price':
                total.text=spec.text
    
        qte=etree.Element('qte')
        qte.text='1'
        computer.append(total)
        computer.append(qte)
        cart.append(computer)
 
        totals= next(t for t in cart if t.tag=='total')
   
        print(totals.text)
        totals.text=str(float(totals.text)+float(total.text))
        cart.getroottree().write(r"D:\ComputerStore\carts\database\carts.xml")
        cart.getroottree().write(cartv)
        return HttpResponse("Item added")
    
def handle_change_qte(request):
    if request.method == 'POST':
        if validate(request.body) == False:
            return HttpResponseBadRequest("Invalid input")
        userId=getinput().getroot().get('userId')
        compId=getinput().getroot()[0].get('id')
        newqte=getinput().getroot()[0].text
        users=connect_db('users')
        if bool(users.getroot().xpath("/users/user[@id="+str(userId)+"]"))==False:
            return HttpResponseBadRequest("User Does Not Exist")
        cart=get_user_cart(userId)

        if bool(cart.xpath('computer[@id='+str(compId)+']'))== False:
            return HttpResponseBadRequest("Add it first")
        if int(newqte)==0:
            computer=cart.xpath('computer[@id='+str(compId)+']')[0]
            cptotal=next(elt for elt in computer if elt.tag=='total')
            ctotal=next(elt for elt in cart if elt.tag=='total')
            ctotal.text=str(float(ctotal.text)-float(cptotal.text))
            computer.getparent().remove(computer)
            cart.getroottree().write(r"D:\ComputerStore\carts\database\carts.xml")
            carts_schema.validate(r"D:\ComputerStore\carts\database\carts.xml")
            return HttpResponse("Item deleted")
        
        computer=cart.xpath('computer[@id='+str(compId)+']')[0]
        qte=next(elt for elt in computer if elt.tag=='qte')
        cptotal=next(elt for elt in computer if elt.tag=='total')
        price=next(elt for elt in computer if elt.tag=='price')
        ctotal=next(elt for elt in cart if elt.tag=='total')
        ctotal.text=str(float(ctotal.text)-float(cptotal.text))
        cptotal.text=str(float(cptotal.text)+(int(newqte)-int(qte.text))*float(price.text))
        ctotal.text=str(float(ctotal.text)+float(cptotal.text))
        qte.text=newqte

        cart.getroottree().write(r"D:\ComputerStore\carts\database\carts.xml")
        carts_schema.validate(r"D:\ComputerStore\carts\database\carts.xml")
        return HttpResponse("Item quantity changed")


