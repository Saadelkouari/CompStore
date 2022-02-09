from django.urls import path
from . import views

urlpatterns =[
    path('createinvoice/',views.create_invoice),
    path('getinvoices/',views.get_invoices),
    path('printinvoice/',views.print_invoice),
    #path('desktops/',views.get_desktops),
    
]