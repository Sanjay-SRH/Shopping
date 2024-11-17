from datetime import datetime

class Product:
    """Base class for all products."""
    next_id = 1  # Static variable to auto-generate product IDs

    def __init__(self, name, price, quantity=1):
        self.product_id = Product.next_id
        Product.next_id += 1
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_subtotal(self):
        """Calculate the subtotal for the product based on quantity."""
        return self.price * self.quantity

    def get_details(self):
        """Return product details as a dictionary."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def __str__(self):
        """String representation of the product."""
        return f"{self.name} (ID: {self.product_id}) - ${self.price} x {self.quantity}"


class Electronics(Product):
    """Electronics category with additional attributes."""
    def __init__(self, name, price, warranty_period, brand, quantity=1):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period  # In months
        self.brand = brand

    def get_details(self):
        """Include electronics-specific details."""
        details = super().get_details()
        details.update({
            "warranty_period": self.warranty_period,
            "brand": self.brand
        })
        return details


class Clothing(Product):
    """Clothing category with additional attributes."""
    def __init__(self, name, price, size, color, fabric_type, quantity=1):
        super().__init__(name, price, quantity)
        self.size = size
        self.color = color
        self.fabric_type = fabric_type

    def get_details(self):
        """Include clothing-specific details."""
        details = super().get_details()
        details.update({
            "size": self.size,
            "color": self.color,
            "fabric_type": self.fabric_type
        })
        return details


class Groceries(Product):
    """Groceries category with additional attributes."""
    def __init__(self, name, price, expiration_date, packaging_type, quantity=1):
        super().__init__(name, price, quantity)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        self.packaging_type = packaging_type

    def is_expired(self):
        """Check if the grocery item is expired."""
        return self.expiration_date < datetime.today().date()

    def get_details(self):
        """Include groceries-specific details."""
        details = super().get_details()
        details.update({
            "expiration_date": self.expiration_date,
            "packaging_type": self.packaging_type
        })
        return details


class ModelDataSaver:
    """Class to save product data into models.txt."""
    
    @staticmethod
    def save_to_file(products, filename="models.txt"):
        """Save product data to a file in a tabular format."""
        try:
            with open(filename, "a") as file:  # Open in append mode ('a')
                # Write the header for the table only if the file is empty
                file.seek(0, 2)  # Move to the end of the file
                if file.tell() == 0:  # Check if the file is empty
                    file.write(f"{'Category':<15}|{'Product ID':<12}|{'Name':<20}|{'Price':<10}|{'Quantity':<10}|{'Details':<30}\n")
                    file.write("=" * 80 + "\n")

                # Write each product's details in tabular format
                for product in products:
                    details = product.get_details()
                    if isinstance(product, Electronics):
                        extra_details = f"Warranty: {details['warranty_period']}M, Brand: {details['brand']}"
                        category = "Electronics"
                    elif isinstance(product, Clothing):
                        extra_details = f"Size: {details['size']}, Color: {details['color']}, Fabric: {details['fabric_type']}"
                        category = "Clothing"
                    elif isinstance(product, Groceries):
                        extra_details = f"Expiry: {details['expiration_date']}, Packaging: {details['packaging_type']}"
                        category = "Groceries"
                    else:
                        extra_details = "N/A"
                        category = "General"

                    file.write(f"{category:<15}|{details['product_id']:<12}|{details['name']:<20}|${details['price']:<9.2f}|{details['quantity']:<10}|{extra_details:<30}\n")

                # Indicate completion
                file.write("=" * 80 + "\n")
            print(f"Product data appended to {filename} in tabular format.")
        except Exception as e:
            print(f"An error occurred while saving the product data: {e}")


# Example of adding products and saving to models.txt
electronics = Electronics(name="Smart TV", price=500.00, warranty_period=24, brand="Samsung", quantity=2)
clothing = Clothing(name="T-Shirt", price=20.00, size="M", color="Red", fabric_type="Cotton", quantity=3)
groceries = Groceries(name="Milk", price=3.00, expiration_date="2024-11-20", packaging_type="Carton", quantity=5)

# Save the products to models.txt
ModelDataSaver.save_to_file([electronics, clothing, groceries])
