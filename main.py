from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()
cart = Cart()

product1 = Product("Gaming Laptop", 4500, 5)
product2 = Product("SmartPhone", 3000, 7)
product3 = Product("Wireless Headphones", 500, 13)
product4 = Product("Mouse", 150, 7)
product5 = Product("Keyboard", 200, 4)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)

print("Available Products:")
manager.display_products()

random_products = random.sample(manager.products, 3)
for product in random_products:
    cart.add_to_cart(product, random.randint(1, product.quantity))

cart.display_cart()