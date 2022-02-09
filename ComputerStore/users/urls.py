from django.urls import path
from . import views

urlpatterns =[
    path('register/',views.handle_register),
    path('login/',views.handle_login),
    path('getuser/',views.getuserinfo)
]