
from django.contrib import admin
from django.urls import path,include
from .views import home,product,about

urlpatterns = [
   path('',home,name='home'),
   path('products',product,name='product'),
   path('about',about,name='about'),
]
