import json

products = []
for i in range(10):
    pid = input("Enter Product ID: ")
    pname = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = input("Enter Price: ")
    quantity = input("Enter Quantity Available: ")
    products.append({
        "Product ID": pid,
        "Product Name": pname,
        "Category": category,
        "Price": price,
        "Quantity Available": quantity
    })

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

print("✅ products.json created successfully!")
