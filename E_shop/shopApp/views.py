from django.shortcuts import render,HttpResponse
from django.http import request

from .models import Product,Category

# Create your views here.
def home(request): # this is home page view
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,"shop/home.html",context={'products':products,'categories':categories})

def getCategoryData(request,name): # this is home page view
    categories=Category.objects.all()
    category_searched=Category.objects.get(name=name)
    certain_category_entries=Product.objects.filter(category=category_searched.id)
    return render(request,"shop/home.html",context={'products':certain_category_entries,'categories':categories})



def product(request): #this is products page view
    return render(request,"shop/product.html")

def about(request): # this is about page view
    return render(request,"shop/about.html")


def contact(request): # this is contact page view
    return render(request,"shop/contact.html")