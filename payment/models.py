from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save

class ShippingAddress(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
     shipping_full_name = models.CharField(max_length=255)
     shipping_email = models.CharField(max_length=20 , blank=True)
     shipping_address1 = models.CharField(max_length=200 , blank=True)
     shipping_address2 = models.CharField(max_length=200 , blank=True,null=True)
     shipping_city = models.CharField(max_length=200 , blank=True,null=True,)
     shipping_zipcode = models.CharField(max_length=200 , blank=True,null=True,)
     shipping_country = models.CharField(max_length=200 , blank=True)
     

     class Meta :
         verbose_name_plural = "Shipping Address"


     def __str__(self):
          return f'Shipping address - {str(self.id)}'
     

# Create user profile by deafult
def create_shipping(sender ,instance , created,**kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping,sender=User)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=20 , blank=True)     
    shipping_address = models.CharField(max_length=200 , blank=True)
    amount_paid = models.DecimalField(
        max_digits=12,  
        decimal_places=0,
        default= 0 ,
    )
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"orser {str(self.id)}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(
        max_digits=12,  
        decimal_places=0,
        default= 0 ,
    )


    def __str__(self):
         return f'order item {str(self.id)}'