
import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @classmethod
    def deserialize(cls, json_str):
        attributes = json.loads(json_str)
        return cls(**attributes)

def write_products_to_file(products, filename):
    with open(filename, 'w') as file:
        # Convert each product to its JSON string representation and write it to the file
        json_list = [product.serialize() for product in products]
        json_str = json.dumps(json_list)
        file.write(json_str)

def read_products_from_file(filename):
    with open(filename, 'r') as file:
        json_str = file.read()
        products_dict_list = json.loads(json_str)
        return [Product.deserialize(json.dumps(product_dict)) for product_dict in products_dict_list]

# Create several Product objects
products = [
    Product("Laptop", 1200, 5),
    Product("Smartphone", 800, 10),
    Product("Headphones", 150, 15)
]

# Write the products to a file
write_products_to_file(products, 'products.json')

# Read the products from the file
deserialized_products = read_products_from_file('products.json')

# Print all the product information
for product in deserialized_products:
    print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
