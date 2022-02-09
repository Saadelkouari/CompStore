from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseBadRequest
from lxml import etree
import xmlschema
from io import StringIO
# Create your views here.
db=r"D:\ComputerStore\users\database\users.xml"
userv=r"D:\ComputerStore\users\database\userv.xml"
users_schema=r"D:\ComputerStore\users\database\users.xsd"
def connect_db(name):
    fcarts=open("D:\\ComputerStore\\"+name+"\\database\\"+name+".xml","r")
    carts=fcarts.read()
    fcarts.close()
    return etree.parse(StringIO(carts))
def validate(body):
    f=open(userv,'w')
    body_unicode = body.decode('utf-8')
    f.write(body_unicode)
    f.close()
    try:
        users_schema.validate(userv)
        return True
    except Exception as e:
        print(e)
def getinput():
    f=open(userv,'r')
    input=f.read()
    f.close()
    return etree.parse(StringIO(input))

def handle_register(request):
    if request.method == 'POST':
        userv_schema=xmlschema.XMLSchema11(r"D:\ComputerStore\users\database\userv.xsd")
        f=open(r"D:\ComputerStore\users\database\userv.xml",'w')
        body_unicode = request.body.decode('utf-8')
        f.write(body_unicode)
        f.close()
        
        try:
            userv_schema.validate(r"D:\ComputerStore\users\database\userv.xml")
            f=open(r"D:\ComputerStore\users\database\userv.xml","r")
            userv=f.read()
            f.close()
            newuser = etree.parse(StringIO(userv))
            f=open(r'D:\ComputerStore\users\database\users.xml',"r")
            users=f.read()
            f.close()
            users=etree.parse(StringIO(users))
            i=0
            for user in users.getroot():
                i = int(user.get('id')) if int(user.get('id')) > i else i
            newuser=newuser.getroot()
            newuser.set('id',str(i+1))
            users.getroot().append(newuser)
            users.write(r'D:\ComputerStore\users\database\usersv.xml')
            usersv_schema=xmlschema.XMLSchema11(r"D:\ComputerStore\users\database\users.xsd")
            usersv_schema.validate(r"D:\ComputerStore\users\database\usersv.xml")
            users.write(r'D:\ComputerStore\users\database\users.xml')
            return HttpResponse()
        except Exception as e:
          return HttpResponseBadRequest(e)

def handle_login(request):
    if request.method == 'POST':
        userv_schema=xmlschema.XMLSchema11(r"D:\ComputerStore\users\database\userv.xsd")
        f=open(r"D:\ComputerStore\users\database\userv.xml",'w')
        body_unicode = request.body.decode('utf-8')
        f.write(body_unicode)
        f.close()
        try:
            userv_schema.validate(r"D:\ComputerStore\users\database\userv.xml")
            f=open(r"D:\ComputerStore\users\database\userv.xml","r")
            userv=f.read()
            f.close()
            login = etree.parse(StringIO(userv))
            users=open(r'D:\ComputerStore\users\database\users.xml',"r")
            users=users.read()
            users=etree.parse(StringIO(users))
            for user in users.getroot().xpath('/users/user'):
                if user.xpath('email')[0].text == login.getroot().xpath('/login/email')[0].text:
                    if login.getroot().xpath('password')[0].text==user.xpath('password')[0].text:
                        ide=user.get('id')
                        return HttpResponse(ide)
            return HttpResponseBadRequest("User Not Found")    
        except:
             return HttpResponseBadRequest('Invalid email or password')

def getuserinfo(request):
    if request.method=='POST':
        if validate(request.body)==False:
            return HttpResponseBadRequest("Invalide input.")
        userId=getinput().getroot().text
        users=connect_db('users')
        if bool(users.getroot().xpath('/users/user[@id='+str(userId)+']')):
            usersv=etree.Element('users')
            usersv.append(users.xpath('/users/user[@id='+str(userId)+']')[0])
            usersv.getroottree().write(userv)
            return HttpResponse(open(r'D:\ComputerStore\users\database\userv.xml','r').read(),content_type='application/xml')
        return HttpResponseBadRequest('User does not exist')


    return 0