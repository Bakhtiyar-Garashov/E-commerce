
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from .views import home,product,about,contact,getCategoryData

urlpatterns = [
   path('',home,name='home'),
   path('products',product,name='product'),
   path('about',about,name='about'),
   path('contact',contact,name='contact'),
   path('categories/<str:name>',getCategoryData,name='getCategoryData'),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)