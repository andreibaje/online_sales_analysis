from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"Product '{product_name}' has been removed.")
                return
        print(f"Product '{product_name}' not found.")

    def display_products(self):
        if not self.products:
            print("No products available.")
        for product in self.products:
            print(product.display_info())

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)