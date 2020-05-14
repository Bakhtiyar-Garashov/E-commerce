from django.shortcuts import render,HttpResponse

from .models import Product

# Create your views here.
def home(request): # this is home page view
    products=Product.objects.all()
    return render(request,"shop/home.html",context={'products':products})


def product(request): #this is products page view
    return render(request,"shop/product.html")

def about(request): # this is about page view
    return render(request,"shop/about.html")


def contact(request): # this is contact page view
    return render(request,"shop/contact.html")