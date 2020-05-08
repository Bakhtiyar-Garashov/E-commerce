from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request): # this is home page view
    return render(request,"shop/home.html")


def product(request): #this is products page view
    return render(request,"shop/product.html")

def about(request): # thos is about page view
    return render(request,"shop/about.html")


def contact(request):
    return render(request,"shop/contact.html")