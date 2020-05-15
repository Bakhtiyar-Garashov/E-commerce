from django.db import models

from accounts.models import Customer


#models related to ShopApp
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"



class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField(default="Some dummy desc for development stage")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    #image
    isAvailable=models.BooleanField(default=False,verbose_name="Available")

    def __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    isCompleted=models.BooleanField(default=False,verbose_name="Completed")
    transactionId=models.CharField(max_length=120)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    

class ShippingDetail(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=20)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name+"'s shipping details"
    
