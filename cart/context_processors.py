from .cart import Cart

# Create context processors

def cart(request):

     return {'cart' : Cart(request)}