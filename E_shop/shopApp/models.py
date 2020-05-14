from django.db import models

from ..accounts.models import Customer

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    #image
    isAvailable=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL)
    date=models.DateTimeField(auto_now_add=True)
    isCompleted=models.BooleanField(default=False)
    transactionId=models.CharField(max_length=120)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    

class ShippingDetails(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL)
    address=models.CharField(max_length=200)
    city=models.CharField(max_lenght=50)
    zipcode=models.CharField(max_length=20)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name+"'s shipping details"
    
