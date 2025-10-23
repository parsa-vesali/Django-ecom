from django.shortcuts import render
from cart.cart import Cart

from payment.forms import shippingForm , ShippingAddress

def checkout(request):
     # Get cart
     cart = Cart(request)
     cart_products = cart.get_prods()
     quantities = cart.get_quants
     totals = cart.cart_total()
     shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)

     if request.user.is_authenticated:
          shipping_form = shippingForm(request.POST or None, instance=shipping_user)
          return render(request , "payment/checkout.html" , {"cart_products" : cart_products , "quantities" : quantities ,"totals" : totals , 'shipping_form' : shipping_form})
     else:
          shipping_form = shippingForm(request.POST or None)
          return render(request , "payment/checkout.html" , {"cart_products" : cart_products , "quantities" : quantities ,"totals" : totals, 'shipping_form' : shipping_form})


def payment_success(request):
     return render(request,"payment/payment_success.html" , {})