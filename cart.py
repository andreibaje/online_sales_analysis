from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        if quantity > product.quantity:
            print(f"Not enough stock for {product.name}. Available: {product.quantity}")
        else:
            self.cart_items.append((product, quantity))
            product.quantity -= quantity  # Reduce stock from inventory
            print(f"Added {quantity} x {product.name} to cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("\nCart Contents:")
            for product, quantity in self.cart_items:
                print(f"{quantity} x {product.name} - {product.price} RON each")
            print(f"Total: {self.calculate_total()} RON")