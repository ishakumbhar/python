product_names = []
product_prices = []
product_qty = []

while True:
    print("=" * 45)
    print("       PRODUCT INVENTORY SYSTEM")
    print("=" * 45)
    print("1. Add Product")
    print("2. Delete Product")
    print("3. Display All Products")
    print("4. Exit")
    print("=" * 45)

    choice = input("Enter your choice (1-4): ").strip()

    # 1. ADD PRODUCT
    if choice == '1':
        name = input("Enter Product Name: ").strip()

        if name in product_names:
            print(f"Product '{name}' already exists!\n")
        else:
            try:
                price = float(input(f"Enter price for {name}: "))
                qty = int(input(f"Enter quantity for {name}: "))

                if price < 0 or qty < 0:
                    print("Price and quantity cannot be negative.\n")
                else:
                    product_names.append(name)
                    product_prices.append(price)
                    product_qty.append(qty)

                    print(f"Product '{name}' added successfully!\n")

            except ValueError:
                print("Please enter a valid price and quantity.\n")

    # 2. DELETE PRODUCT
    elif choice == '2':
        name = input("Enter Product Name to delete: ").strip()

        if name in product_names:
            index = product_names.index(name)

            product_names.pop(index)
            product_prices.pop(index)
            product_qty.pop(index)

            print(f"Product '{name}' deleted successfully!\n")

        else:
            print(f"Product '{name}' not found.\n")

    # 3. DISPLAY PRODUCTS
    elif choice == '3':
        if len(product_names) == 0:
            print("No products to display.\n")

        else:
            print("\n" + "=" * 55)
            print(
                "{:<5} {:<20} {:<12} {:<10}".format(
                    "No.", "Name", "Price", "Qty"
                )
            )
            print("-" * 55)

            for i in range(len(product_names)):
                print(
                    "{:<5} {:<20} ₹{:<11.2f} {:<10}".format(
                        i + 1,
                        product_names[i],
                        product_prices[i],
                        product_qty[i]
                    )
                )

            print("=" * 55)
            print()

    # 4. EXIT
    elif choice == '4':
        print("Exiting program. Thank you!")
        break

    # INVALID CHOICE
    else:
        print("Invalid choice. Please enter a number between 1 and 4.\n")
