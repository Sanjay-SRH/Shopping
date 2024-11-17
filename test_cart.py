# test_cart.py

from models import Electronics, Clothing, Groceries
from cart import Cart

# Create sample products
tv = Electronics(name="Smart TV", price=500, warranty_period=24, brand="Samsung", quantity=1)
jeans = Clothing(name="Jeans", price=40, size="M", color="Blue", fabric_type="Denim", quantity=2)
milk = Groceries(name="Milk", price=3, expiration_date="2024-11-20", packaging_type="Carton", quantity=5)

# Create a cart instance
my_cart = Cart()

# Add items to the cart
my_cart.add_item(tv)
my_cart.add_item(jeans)
my_cart.add_item(milk)

# View the cart
my_cart.view_cart()

# Update quantity
my_cart.update_quantity(tv.product_id, 2)
my_cart.view_cart()

# Remove an item
my_cart.remove_item(jeans.product_id)
my_cart.view_cart()

# Apply a discount
my_cart.apply_discount(10)

# Save and load the cart
my_cart.save_cart()
my_cart.load_cart()
my_cart.view_cart()
