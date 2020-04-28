from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"shop/index.html")


def product(request):
    return render(request,"shop/product.html")