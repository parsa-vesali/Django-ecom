from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
     full_name = models.CharField(max_length=255)
     email = models.CharField(max_length=20 , blank=True)
     address1 = models.CharField(max_length=200 , blank=True)
     address2 = models.CharField(max_length=200 , blank=True,null=True)
     city = models.CharField(max_length=200 , blank=True,null=True,)
     zipcode = models.CharField(max_length=200 , blank=True,null=True,)
     country = models.CharField(max_length=200 , blank=True)
     

     class Meta :
         verbose_name_plural = "Shipping Address"


     def __str__(self):
          return f'Shipping address - {str(self.id)}'