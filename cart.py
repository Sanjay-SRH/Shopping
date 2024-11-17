from models import Product, Electronics, Clothing, Groceries

class Cart:
    """Class to manage the shopping cart."""
    
    def __init__(self):
        self.items = []  # List to store Product objects

    def add_item(self, product):
        """Add a product to the cart."""
        self.items.append(product)
        print(f"{product.name} added to the cart!")

    def remove_item(self, product_id):
        """Remove a product from the cart by its product_id."""
        for item in self.items:
            if item.product_id == product_id:
                self.items.remove(item)
                print(f"{item.name} removed from the cart.")
                return
        print(f"Product with ID {product_id} not found in the cart.")

    def update_quantity(self, product_id, quantity):
        """Update the quantity of a product in the cart."""
        for item in self.items:
            if item.product_id == product_id:
                if quantity > 0:
                    item.quantity = quantity
                    print(f"Updated {item.name}'s quantity to {quantity}.")
                else:
                    self.remove_item(product_id)
                return
        print(f"Product with ID {product_id} not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of all items in the cart."""
        return sum(item.calculate_subtotal() for item in self.items)

    def apply_discount(self, discount_percent):
        """Apply a discount to the total."""
        total = self.calculate_total()
        discounted_total = total - (total * discount_percent / 100)
        print(f"Discount applied! Total after {discount_percent}% discount: ${discounted_total:.2f}")
        return discounted_total

    def save_cart(self, filename="cart.txt"):
        """Save the cart to an existing plain text file in a tabular format, appending data."""
        try:
            with open(filename, "a") as file:  # Open in append mode ('a')
                # Write the header for the table only if the file is empty
                file.seek(0, 2)  # Move to the end of the file
                if file.tell() == 0:  # Check if the file is empty
                    file.write(f"{'Category':<15}|{'Product ID':<12}|{'Name':<20}|{'Price':<10}|{'Quantity':<10}|{'Details':<30}\n")
                    file.write("=" * 80 + "\n")

                # Write each item's details in tabular format
                for item in self.items:
                    details = item.get_details()
                    if isinstance(item, Electronics):
                        extra_details = f"Warranty: {details['warranty_period']}M, Brand: {details['brand']}"
                        category = "Electronics"
                    elif isinstance(item, Clothing):
                        extra_details = f"Size: {details['size']}, Color: {details['color']}, Fabric: {details['fabric_type']}"
                        category = "Clothing"
                    elif isinstance(item, Groceries):
                        extra_details = f"Expiry: {details['expiration_date']}, Packaging: {details['packaging_type']}"
                        category = "Groceries"
                    else:
                        extra_details = "N/A"
                        category = "General"

                    file.write(f"{category:<15}|{details['product_id']:<12}|{details['name']:<20}|${details['price']:<9.2f}|{details['quantity']:<10}|{extra_details:<30}\n")

                # Indicate completion
                file.write("=" * 80 + "\n")
            print(f"Cart data appended to {filename} in tabular format.")
        except Exception as e:
            print(f"An error occurred while saving the cart: {e}")

    def load_cart(self, filename="cart.txt"):
        """Load the cart from a plain text file."""
        try:
            with open(filename, "r") as file:
                self.items = []
                for line in file:
                    line = line.strip()  # Remove leading and trailing whitespaces
                    
                    # Skip empty lines or separator lines (e.g., "=====")
                    if not line or line.startswith("="):
                        continue
                    
                    # Split line into parts using the '|' delimiter
                    data = line.split("|")
                    
                    if len(data) < 6:  # Ensure that there are at least 6 parts (Category, ID, Name, Price, Quantity, Details)
                        print(f"Skipping invalid line: {line}")
                        continue
                    
                    category = data[0].strip()
                    product_id = int(data[1].strip())
                    name = data[2].strip()
                    price_str = data[3].strip().replace("$", "")  # Remove dollar sign
                    price = float(price_str) if price_str else 0.0
                    quantity = int(data[4].strip())
                    details = data[5].strip()
                    
                    # Create objects based on category
                    if category == "Electronics":
                        self.items.append(Electronics(name, price, quantity, details, product_id))
                    elif category == "Clothing":
                        self.items.append(Clothing(name, price, quantity, details, product_id))
                    elif category == "Groceries":
                        self.items.append(Groceries(name, price, quantity, details, product_id))
                    else:
                        self.items.append(Product(name, price, quantity, product_id))

            print("Cart loaded successfully.")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty cart.")
        except Exception as e:
            print(f"An error occurred while loading the cart: {e}")

    def view_cart(self):
        """Print all items in the cart."""
        if not self.items:
            print("Your cart is empty!")
            return
        print("Items in your cart:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")
