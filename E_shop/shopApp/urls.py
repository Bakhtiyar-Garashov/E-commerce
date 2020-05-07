
from django.contrib import admin
from django.urls import path,include
from .views import index,product,about

urlpatterns = [
   path('',index,name='home'),
   path('products',product,name='product'),
   path('about',about,name='about'),
]
