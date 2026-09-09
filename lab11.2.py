

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9-10", "10-11", "11-12", "12-1", "1-2"]


schedule = [["-" for day in days] for hour in hours]

while True:
    print("\n===== CLASS SCHEDULE =====")
    print("1. View Schedule")
    print("2. Add/Overwrite Subject")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nTime\t", end="")
        for day in days:
            print(day[:3], "\t", end="")
        print()

        for i in range(len(hours)):
            print(hours[i], "\t", end="")
            for j in range(len(days)):
                print(schedule[i][j], "\t", end="")
            print()

    elif choice == 2:
        print("\nDays:")
        for i in range(len(days)):
            print(i + 1, ".", days[i])

        day = int(input("Select day (1-5): "))
        hour = int(input("Select hour slot (1-5): "))
        subject = input("Enter subject/topic: ")

        if 1 <= day <= 5 and 1 <= hour <= 5:
            schedule[hour - 1][day - 1] = subject
            print("Schedule updated successfully!")
        else:
            print("Invalid selection!")

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")