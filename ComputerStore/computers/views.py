import shutil
from django.http import FileResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import re
import sys,os
sys.path.append('C:\Program Files\Saxonica\SaxonHEC1.2.1\Saxon.C.API\python-saxon')
# Create your views here.

@api_view()
def getcomputers(request):
    if request.method == 'GET':
        for filter in request.GET.keys():
            os.system('python D:\ComputerStore\computers\queryfiltering.py '+str(filter)+' '+str(request.GET['filter']))

    return 0
def get_computers(request):

    if request.method == 'GET':
        if request.GET:
            if request.GET['op']=="gt":
                os.system('python D:\ComputerStore\computers\queryfiltering.py '+str(request.GET['filter'])+' gt '+str(request.GET['value']))
                
                return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')
            if request.GET['op']=="lt":
                os.system('python D:\ComputerStore\computers\queryfiltering.py '+str(request.GET['filter'])+' ls '+str(request.GET['value']))
                
                return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')
            if request.GET['op']=='=':
                os.system('python D:\ComputerStore\computers\queryfiltering.py '+str(request.GET['filter'])+" "+str(request.GET['op'])+" "+str(request.GET['value']))
                return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')
        shutil.copyfile('D:\ComputerStore\computers\database\computers.xml','D:\ComputerStore\computers\query.xml')
        return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')
    
    
@api_view()
def get_computer(request,id):
    os.system('python D:\ComputerStore\computers\query.py '+str(id))
    return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')

@api_view()
def get_laptops(request):
    os.system('python D:\ComputerStore\computers\query_type.py laptop')
    
    return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')

@api_view()
def get_desktops(request):
    os.system('python D:\ComputerStore\computers\query_type.py desktop')
    
    return HttpResponse(open('D:\ComputerStore\computers\query.xml','r').read(),content_type='application/xml')
def print_catalog(request):
    if request.method =='GET':
        os.chdir(r"C:\Users\saade\Downloads\fop-2.7-bin\fop-2.7\fop")
        os.system(r".\fop -xml D:\ComputerStore\computers\query.xml -xsl D:\ComputerStore\computers\database\computers.xsl -pdf D:\ComputerStore\computers\database\catalogue.pdf")
        return FileResponse(open(r'D:\ComputerStore\computers\database\catalogue.pdf','rb'))
    