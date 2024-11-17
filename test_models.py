from models import Electronics, Clothing, Groceries

# Create some sample products
tv = Electronics(name="Smart TV", price=500, warranty_period=24, brand="Samsung", quantity=1)
jeans = Clothing(name="Jeans", price=40, size="M", color="Blue", fabric_type="Denim", quantity=2)
milk = Groceries(name="Milk", price=3, expiration_date="2024-11-20", packaging_type="Carton", quantity=5)

# Print product details
print(tv)
print(tv.get_details())
print()

print(jeans)
print(jeans.get_details())
print()

print(milk)
print(milk.get_details())
print(f"Is Milk Expired? {'Yes' if milk.is_expired() else 'No'}")
