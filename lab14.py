print("=" * 50)
print("PHONEBOOK / WORD FREQUENCY COUNTER APP")
print("=" * 50)

phonebook = {}
word_freq = {}

while True:
    print("\n------ MAIN MENU ------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Word Frequency / Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        print("\n---------- ADD CONTACT ----------")

        name = input("Enter contact name: ").strip()

        if name in phonebook:
            print(f"'{name}' already exists with number {phonebook[name]}.")
        else:
            number = input("Enter contact number: ").strip()
            phonebook[name] = number
            print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        print("\n---------- SEARCH CONTACT ----------")

        name = input("Enter name to search: ").strip()

        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        else:
            print(f"'{name}' not found in phonebook.")

    elif choice == "3":
        print("\n---------- DISPLAY ALL CONTACTS ----------")

        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            print("\n{:<20} {:<15}".format("Name", "Contact Number"))
            print("-" * 35)

            for name in phonebook:
                print("{:<20} {:<15}".format(name, phonebook[name]))

    elif choice == "4":
        print("\n---------- WORD FREQUENCY ----------")

        paragraph = input("Enter a paragraph to analyze: ").strip()
        paragraph = paragraph.lower()

        for symbol in [".", ",", "!", "?", ";", ":", '"', "'", "(", ")"]:
            paragraph = paragraph.replace(symbol, "")

        words = paragraph.split()
        word_freq = {}

        for word in words:
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1
            else:
                word_freq[word] = 1

        print("\nWord Frequency:")
        print("{:<20} {:<10}".format("Word", "Frequency"))
        print("-" * 30)

        for word in word_freq:
            print("{:<20} {:<10}".format(word, word_freq[word]))

        print("\nThank you for using the application!")
        print("Goodbye.")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.")
