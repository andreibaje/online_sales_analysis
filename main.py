from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 4500, 3)
product2 = Product("Phone", 3000, 5)
product3 = Product("Headphones", 500, 10)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Available Products:")
manager.display_products()

print("\nRemoving 'Phone'...")
manager.remove_product("Phone")

print(f"\nTotal Value: {manager.total_inventory_value()} RON")