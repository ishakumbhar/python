

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Printer",
    "Headphones",
    "Webcam",
    "Speaker"
]

print("===== INVENTORY CATALOG =====")

print("\nAvailable Products:")
for i in range(len(products)):
    print(i, ":", products[i])


search_item = input("\nEnter the product name to search: ")


found = False

for i in range(len(products)):
    if products[i].lower() == search_item.lower():
        print("\nProduct found!")
        print("Product Name :", products[i])
        print("Index        :", i)
        found = True
        break

if found == False:
    print("\nProduct not found in the inventory.")