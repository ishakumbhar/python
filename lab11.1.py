

seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]


print("Movie Theatre Seating:")
for row in seats:
    print(" ".join(row))


row = int(input("Enter row (1-3): "))
col = int(input("Enter column (1-3): "))


if row < 1 or row > 3 or col < 1 or col > 3:
    print("Invalid seat selection!")
elif seats[row - 1][col - 1] == "X":
    print("Seat is already reserved!")
else:
    seats[row - 1][col - 1] = "X"
    print("Seat reserved successfully!")


print("\nUpdated Seating:")
for row in seats:
    print(" ".join(row))