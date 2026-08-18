print("Monthly Expense Tracker")
step1 = "Enter the number of initial expense"
n = int(input("Enter the number of expense:"))

expenses = []
total = 0

#step2: Record initial expenses using loop
for i in range(n):
    amount = float(input(f"Enter expense {i+1}: "))  #string value accept
    expenses.append(amount)
    total += amount  #append/add all expenses / accumulation logic

#step3: continue until the user chooses to exit
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Show all Expenses")
    print("2. Show Total Expenses")
    print("3. Add New Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nExpense List:")
        print("Expense List:")
        for i in range(len(expenses)):
            print(f"Expense {i+1}: {expenses[i]}")

    elif choice == "2":
        print("Total Monthly Expense:", total)

    elif choice == "3":
        new_expense = float(input("Enter the new expense amount: "))
        expenses.append(new_expense)
        total += new_expense  #accumulation logic
        print("Expense added successfully.")

    elif choice == "4":
        print("Thank you for using the Monthly Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
