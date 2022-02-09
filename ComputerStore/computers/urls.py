from django.urls import path
from . import views

urlpatterns =[
    path('',views.get_computers),
    path('d/',views.getcomputers),
    path('<int:id>',views.get_computer),
    path('laptops/',views.get_laptops),
    path('desktops/',views.get_desktops),
    path('print/',views.print_catalog)
]