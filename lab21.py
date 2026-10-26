DATA_FILE = "attendance.txt"
MIN_PERCENTAGE = 75       
def load_attendance():
    """Reads attendance.txt and returns the attendance dictionary.
    Returns an empty dictionary if the file does not exist yet."""
    attendance = {}
    try:
        file = open(DATA_FILE, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parts = line.split("|")
            roll = parts[0]
            name = parts[1]
            if parts[2] == "":
                records = []                   
            else:
                records = parts[2].split(",")      
            attendance[roll] = [name, records]
    except FileNotFoundError:
        pass                                     
    return attendance
def save_attendance(attendance):
    """Writes the whole dictionary back to the file (overwrites old content)."""
    file = open(DATA_FILE, "w")                 
    for roll in attendance:
        name = attendance[roll][0]
        records = attendance[roll][1]
        line = roll + "|" + name + "|" + ",".join(records) + "\n"
        file.write(line)
    file.close()
def calculate_percentage(records):
    """Takes a list of "P"/"A" entries and returns attendance percentage."""
    total_days = len(records)
    if total_days == 0:
        return 0.0
    present_days = records.count("P")         
    percentage = (present_days / total_days) * 100
    return percentage
def get_status(name):
    """Keeps asking until the user enters P or A. Returns 'P' or 'A'."""
    while True:
        status = input(f"  {name} (P/A): ").strip().upper()
        if status == "P" or status == "A":
            return status
        print("  Invalid input! Enter only P (Present) or A (Absent).")
def add_student(attendance):
    """Adds a new student to the attendance dictionary and saves the file."""
    roll = input("Enter roll number: ").strip()
    if roll == "":
        print("Roll number cannot be empty.\n")
        return
    if "|" in roll:
        print("Roll number cannot contain the '|' character.\n")
        return
    if roll in attendance:                        
        print(f"Roll number {roll} already exists ({attendance[roll][0]}).\n")
        return
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.\n")
        return
    name = name.replace("|", "-")                 
    attendance[roll] = [name, []]                  
    save_attendance(attendance)
    print(f"Student '{name}' added successfully.\n")
def mark_attendance(attendance):
    """Marks today's attendance for every student, one by one."""
    if len(attendance) == 0:
        print("No students found. Add students first.\n")
        return
    longest = 0
    for roll in attendance:
        if len(attendance[roll][1]) > longest:
            longest = len(attendance[roll][1])
    day_number = longest + 1
    print(f"\n--- Marking attendance for Day {day_number} ---")
    for roll in attendance:
        name = attendance[roll][0]
        status = get_status(roll + " - " + name)
        attendance[roll][1].append(status)         
    save_attendance(attendance)
    print("Attendance recorded and saved.\n")
def display_attendance(attendance):
    """Displays a summary table of all students."""
    if len(attendance) == 0:
        print("No students found.\n")
        return
    print("\n{:<8} {:<18} {:<9} {:<7} {:<10}".format(
        "Roll", "Name", "Present", "Total", "Percent"))
    print("-" * 55)
    for roll in attendance:
        name = attendance[roll][0]
        records = attendance[roll][1]
        present = records.count("P")
        total = len(records)
        percent = calculate_percentage(records)
        print("{:<8} {:<18} {:<9} {:<7} {:<10}".format(
            roll, name, present, total, f"{percent:.1f}%"))
    print()
def view_student_record(attendance):
    """Shows the day-by-day record of one student."""
    roll = input("Enter roll number: ").strip()
    if roll in attendance:
        name = attendance[roll][0]
        records = attendance[roll][1]
        print(f"\nStudent : {name} (Roll {roll})")
        if len(records) == 0:
            print("No attendance recorded yet.\n")
            return
        for i in range(len(records)):             
            if records[i] == "P":
                word = "Present"
            else:
                word = "Absent"
            print(f"  Day {i + 1}: {word}")
        print(f"Attendance: {calculate_percentage(records):.1f}%\n")
    else:
        print(f"Roll number {roll} not found.\n")
def show_defaulters(attendance):
    """Lists students whose attendance is below the minimum percentage."""
    found = False
    print(f"\nStudents below {MIN_PERCENTAGE}% attendance:")
    for roll in attendance:
        records = attendance[roll][1]
        if len(records) > 0:
            percent = calculate_percentage(records)
            if percent < MIN_PERCENTAGE:
                print(f"  {roll} - {attendance[roll][0]} : {percent:.1f}%")
                found = True
    if not found:
        print("  None. Everyone meets the requirement!")
    print()
def main():
    attendance = load_attendance()     
    print("=" * 45)
    print("     ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 45)
    print(f"{len(attendance)} student(s) loaded from file.")
    while True:
        print("\n1. Add Student")
        print("2. Mark Today's Attendance")
        print("3. Display Attendance Summary")
        print("4. View a Student's Day-wise Record")
        print("5. Show Defaulters (below 75%)")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            add_student(attendance)
        elif choice == '2':
            mark_attendance(attendance)
        elif choice == '3':
            display_attendance(attendance)
        elif choice == '4':
            view_student_record(attendance)
        elif choice == '5':
            show_defaulters(attendance)
        elif choice == '6':
            print("All data is saved in 'attendance.txt'. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main()