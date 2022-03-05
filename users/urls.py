"""Users URLs"""

from unicodedata import name
from django.urls import path

from users import views

urlpatterns =[
    path('', views.home, name='home'),
    path('denuncia/', views.denuncia, name='denuncia'),
    path('terminios/', views.terminos, name='terminos')
]