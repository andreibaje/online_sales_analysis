# Online Sales Analysis

## The Project
The **Online Sales Analysis** project is meant to simulate an online store catalogue. Its functions are made so that it stores the data about what you can find in the online store, and what has been added in the cart by users. There are more settings in case new items are added, removed or in case the quantity changes. You can also find the total value of the products in the inventory, and in the cart

## `Product` class
**`Product`** represents a product included in the online. The code designed for it includes:
- **Atribution**:
  - `name`: name of the product
  - `price`: the price of one quantity of the product
  - `quantity`: the number of this product available
- **Methods**:
  - `display_info()`: Shows the details of the product
  - `update_quantity(new_quantity)`: Registered the new quantity of a product(in case of a change)

## `ProductManager`class
**`ProductManager`** refers to the organisation of the products in the online store. The code designed for it includes:
- **Atributions**:
  - `products`: In this case, it's a list of product appearing in the store
- **Methods**:
  - `add_product(product)`: Adds a product to the product list
  - `display_all_products()`: Shows the overall stock of the store
  - `display_total_value()`: Shows how much the current store is worth
  - `remove_product(product_name)`: Removes a product from the list

## `Cart` class
**`Cart`** is made to store the data of the shopping cart of a client. The code designed for it includes:
- **Atributions**:
  - `cart_items`: List of products added to the cart
- **Methods**:
  - `add_to_cart(product, quantity)`: Adds a product in the *cart_items*
  - `calculate_total()`: Shows how much is the value is held in the shopping cart
  - `display_cart()`: Shows details about existing products and the total worth of the *cart_items*

## Instalations and Use Guide
1. Clone the repo:
   git clone https://github.com/andreibaje/online_sales_analysis.git
2. Run the python program `main.py`

## Used Apps/Technology:
- **Python**
- **Git**