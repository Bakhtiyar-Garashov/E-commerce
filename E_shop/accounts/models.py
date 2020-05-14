from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    #profile_picture
    email=models.EmailField()

    def __str__(self):
        return self.name
