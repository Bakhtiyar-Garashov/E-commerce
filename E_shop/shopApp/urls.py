
from django.contrib import admin
from django.urls import path,include
from .views import index,product,about

urlpatterns = [
   path('',index,name='home'),
   path('products',product,name='home'),
   path('about',about,name='about'),
]
