
from django.contrib import admin
from django.urls import path,include
from .views import index,product

urlpatterns = [
   path('',index,name='home'),
   path('products',product,name='home'),
]
