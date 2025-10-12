from store.models import Product
from decimal import Decimal
from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def delete(self,product):
        product_id =str(product) 

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = Decimal(0)
        
        for key, quantity in self.cart.items():
            key = int(key)
            product = next((p for p in products if p.id == key), None)
            if product:
                total += Decimal(product.final_price) * quantity

        return total
