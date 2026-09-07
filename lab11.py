

ROWS = 5
SEATS_PER_ROW = 4


bus = [[0 for _ in range(SEATS_PER_ROW)] for _ in range(ROWS)]


def display_bus():
    print("\n===== BUS LAYOUT =====")

    for i in range(ROWS):
        print(f"Row {i + 1}: ", end="")

        for j in range(SEATS_PER_ROW):
            if bus[i][j] == 0:
                print(f"[{j + 1}:A]", end=" ")
            else:
                print(f"[{j + 1}:B]", end=" ")

        print()


def reserve_seat():
    display_bus()

    row = int(input("\nEnter row number: "))
    seat = int(input("Enter seat number: "))

    
    if row < 1 or row > ROWS or seat < 1 or seat > SEATS_PER_ROW:
        print("Invalid row or seat number.")
        return

    
    if bus[row - 1][seat - 1] == 1:
        print("Sorry, this seat is already booked.")
    else:
        bus[row - 1][seat - 1] = 1
        print("Seat reserved successfully!")


def cancel_seat():
    display_bus()

    row = int(input("\nEnter row number: "))
    seat = int(input("Enter seat number: "))

    
    if row < 1 or row > ROWS or seat < 1 or seat > SEATS_PER_ROW:
        print("Invalid row or seat number.")
        return

    
    if bus[row - 1][seat - 1] == 0:
        print("This seat is not booked.")
    else:
        bus[row - 1][seat - 1] = 0
        print("Reservation cancelled successfully!")



while True:
    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. Display Bus Layout")
    print("2. Reserve Seat")
    print("3. Cancel Reservation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_bus()

    elif choice == "2":
        reserve_seat()

    elif choice == "3":
        cancel_seat()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")