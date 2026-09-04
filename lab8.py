raw_name = input("Enter Customer Name: ")
raw_feedback = input("Enter Feedback Message: ")
rating = int(input("Enter rating(1 to 5): "))

clean_name = raw_name.strip()
clean_feedback = raw_feedback.strip()

formatted_name = clean_name.title()

formatted_feedback = clean_feedback.capitalize()

formatted_feedback = formatted_feedback.replace(" u ", " You ").replace(" r ", " are ")

exclamation_count = formatted_feedback.count("!")

while True:
    if (rating>=1 and rating<=5):
        if int(rating)>=4:
            category = "POSITIVE".upper()
        else:
            category = "NEEDS REVIEW".upper()
        break
    else:
        rating = int(input("Invalid rating Provided. Enter rating(1 to 5):"))
    

print("\n" + "=" * 45)
print(f"Customer Name  :{formatted_name}")
print(f"Rating         :{rating} / 5 Stars")
print(f"Category         :[{category}]")
print(f"Excitment         :{exclamation_count} exclamation mark(s)")
print("-" * 45)
print("Formatted Message: ")
print(f'"{formatted_feedback}"')
print("-"*45)