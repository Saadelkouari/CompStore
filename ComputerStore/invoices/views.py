from django.shortcuts import render
from copy import deepcopy
from django.http.response import HttpResponse,HttpResponseBadRequest
from lxml import etree
import xml.etree.ElementTree as ET
from io import StringIO
import xmlschema
import sys,os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import FileResponse

sys.path.append('C:\Program Files\Saxonica\SaxonHEC1.2.1\Saxon.C.API\python-saxon')
from saxonc import *
import os
port = 465
password = 'simplepassword'



invoices_schema=xmlschema.XMLSchema11(r'D:\ComputerStore\invoices\database\invoices.xsd')
db=r"D:\ComputerStore\invoices\database\invoices.xml"
invoicev=r"D:\ComputerStore\invoices\database\invoicev.xml"
def connect_db(name):
    fcarts=open("D:\\ComputerStore\\"+name+"\\database\\"+name+".xml","r")
    carts=fcarts.read()
    fcarts.close()
    return etree.parse(StringIO(carts))
def validate(body):
    f=open(invoicev,'w')
    body_unicode = body.decode('utf-8')
    f.write(body_unicode)
    f.close()
    try:
        invoices_schema.validate(invoicev)
        return True
    except Exception as e:
        print(e)
        return False

def getinput():
    f=open(invoicev,'r')
    input=f.read()
    f.close()
    return etree.parse(StringIO(input))

def get_invoices(request):
    if request.method =='POST':
        if validate(request.body)==False:
            return HttpResponseBadRequest("Invalid input")
        userId=getinput().getroot().text
        os.system('python D:\ComputerStore\invoices\query.py '+str(userId))
        return HttpResponse(open('D:\ComputerStore\invoices\database\invoicev.xml','r').readlines()[0],content_type='application/xml')

def create_invoice(request):
    if request.method=='POST':
        if validate(request.body)==False:
            return HttpResponseBadRequest("Invalide input.")
        invoice=getinput().getroot()
        userId=invoice.get('userId')
        users=connect_db('users')
        useremail=users.getroot().xpath('/users/user[@id='+str(userId)+']/email')[0].text
        print(useremail)
        invoices=connect_db('invoices')
        i=0
        for inv in invoices.getroot():
            i = int(inv.get('id')) if int(inv.get('id')) > i else i
        invoice.set('id',str(i+1))
        invoice.getroottree().write(invoicev)
        invoices.getroot().append(invoice)
        invoices.write(db)
        xsltproc = PySaxonProcessor().new_xslt_processor()
        result = xsltproc.transform_to_string(source_file=r"D:\ComputerStore\invoices\database\invoicev.xml", stylesheet_file=r"D:\ComputerStore\invoices\database\invoice.xsl")
        message = MIMEMultipart("alternative")
        message["Subject"] = "Facture ComputerStore"
        message["From"] = "computerstore1447@gmail.com"
        message["To"] = useremail
        part2 = MIMEText(result, "html")
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("computerstore1447@gmail.com", password)
            server.sendmail('computerstore1447@gmail.com',useremail, message.as_string())
        return HttpResponse("Invoice added.")
def delete_invoice(request):
    if request.method =='POST':
        if validate(request.body)==False:
            return HttpResponseBadRequest("Invalid input")
    invoices=connect_db('invoices')
    for invoice in invoices.getroot():
        if invoice.get('id')==getinput().getroot().text:
            invoice.getparent().remove(invoice)
            return HttpResponse("Invoice deleted successfully")
    return HttpResponseBadRequest("Invoice does not exist")

def print_invoice(request):
    if request.method =='POST':
        if validate(request.body)==False:
            HttpResponseBadRequest("Invalid input")
        invoiceId=getinput().getroot().text
        invoice=connect_db('invoices').getroot().xpath('/factures/facture[@id='+str(invoiceId)+']')[0]
        invoicev=deepcopy(invoice)
        invoicev.getroottree().write(r"D:\ComputerStore\invoices\database\invoicev.xml")
        os.chdir(r"C:\Users\saade\Downloads\fop-2.7-bin\fop-2.7\fop")
        os.system(r".\fop -xml D:\ComputerStore\invoices\database\invoicev.xml -xsl D:\ComputerStore\invoices\database\facturefo.xsl -pdf D:\ComputerStore\invoices\database\invoice.pdf")
        return FileResponse(open(r'D:\ComputerStore\invoices\database\invoice.pdf','rb'))
        