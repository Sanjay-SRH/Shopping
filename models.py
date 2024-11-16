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