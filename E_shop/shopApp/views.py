from django.shortcuts import render, HttpResponse
from django.http import request

from .models import Product, Category, Order, OrderItem, ShippingDetail

# Create your views here.


def home(request):  # this is home page view
    products = Product.objects.all()
    categories = Category.objects.all()
    item_total = Order.get_card_items
    return render(request, "shop/home.html", context={'products': products, 'categories': categories, 'total': item_total})


def getCategoryData(request, name):  # this is home page view
    categories = Category.objects.all()
    # first to find category object by name
    category_searched = Category.objects.get(name=name)

    certain_category_entries = Product.objects.filter(
        category=category_searched.id)  # find related products based on category id
    return render(request, "shop/home.html", context={'products': certain_category_entries, 'categories': categories})


def card(request):  # this is card page view
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, isCompleted=False)
        items = order.orderitem_set.all()  # items that related to specific order
    else:
        items = []
        customer = None
        order = {'get_card_total': 0, 'get_card_items': 0}
    context = {'items': items, 'order': order, 'customer': customer}

    return render(request, "shop/card.html", context=context)


def product(request):  # this is products page view
    return render(request, "shop/product.html")


def about(request):  # this is about page view
    return render(request, "shop/about.html")


def contact(request):  # this is contact page view
    return render(request, "shop/contact.html")
