from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Gaming Laptop", 4500, 5)
product2 = Product("SmartPhone", 3000, 7)
product3 = Product("Wireless Headphones", 500, 13)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Available Products:")
manager.display_products()

