from django.contrib import admin
from .models import Product,Order,OrderItem,ShippingDetail

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingDetail)