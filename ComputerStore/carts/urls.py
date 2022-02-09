from django.urls import path
from . import views

urlpatterns =[
    path('getcart/',views.get_cart),
    path('additem/',views.handle_add),
    path('changequantity/',views.handle_change_qte),
    path('emptycart/',views.empty_cart),

    
]