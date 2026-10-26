SCORE_FILE = "quiz_scores.txt"
questions = [
    "Which keyword is used to define a function in Python?",
    "What is the output of len([1, 2, 3, 4])?",
    "Which of the following is a mutable data type?",
    "Which file mode erases the existing content of a file?",
    "What does range(3) generate?"
]
options = [
    ["func", "define", "def", "function"],
    ["3", "4", "5", "Error"],
    ["tuple", "string", "list", "int"],
    ["\"r\"", "\"a\"", "\"w\"", "\"r+\""],
    ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3"]
]
answers = ["C", "B", "C", "C", "B"]
option_letters = ["A", "B", "C", "D"]
def display_question(index):
    """Shows question number (index + 1) and its four options."""
    print(f"\nQ{index + 1}. {questions[index]}")
    for i in range(len(options[index])):                
        print(f"   {option_letters[i]}) {options[index][i]}")
def get_answer():
    """Keeps asking until the user enters a valid option (A/B/C/D).
    Returns the answer in capital letters."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in option_letters:                 
            return answer
        else:
            print("Invalid input! Please enter only A, B, C or D.")
def run_quiz():
    """Asks every question, checks each answer, and returns the final score."""
    score = 0
    for i in range(len(questions)):                     
        display_question(i)
        user_answer = get_answer()
        if user_answer == answers[i]:                     
            print("Correct!")
            score = score + 1
        else:
            print(f"Wrong! The correct answer is {answers[i]}.")
    return score
def get_grade(percentage):
    """Returns a remark based on the percentage scored."""
    if percentage >= 80:
        return "Excellent!"
    elif percentage >= 60:
        return "Good job!"
    elif percentage >= 40:
        return "Average - keep practising."
    else:
        return "Needs improvement - revise and try again."
def save_score(name, score, total):
    """Appends the student's result to the score file."""
    file = open(SCORE_FILE, "a")                          
    file.write(name + "," + str(score) + "," + str(total) + "\n")
    file.close()
def show_past_scores():
    """Reads the score file and displays all saved results."""
    try:
        file = open(SCORE_FILE, "r")
        lines = file.readlines()
        file.close()
        if len(lines) == 0:
            print("\nNo scores saved yet.")
            return
        print("\n{:<20} {:<10}".format("Name", "Score"))
        print("-" * 30)
        for line in lines:
            parts = line.strip().split(",")
            print("{:<20} {:<10}".format(parts[0], parts[1] + "/" + parts[2]))
    except FileNotFoundError:
        print("\nNo scores saved yet. Take the quiz first!")
def main():
    print("=" * 45)
    print("            ONLINE QUIZ SYSTEM")
    print("=" * 45)
    while True:
        print("\n1. Start Quiz")
        print("2. View Past Scores")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            name = input("Enter your name: ").strip()
            if name == "":
                print("Name cannot be empty.")
                continue
            print(f"\nWelcome, {name}! The quiz has {len(questions)} questions.")
            score = run_quiz()
            total = len(questions)
            percentage = (score / total) * 100
            print("\n" + "=" * 45)
            print("               FINAL RESULT")
            print("=" * 45)
            print(f"Name       : {name}")
            print(f"Score      : {score} / {total}")
            print(f"Percentage : {percentage:.1f}%")
            print(f"Remark     : {get_grade(percentage)}")
            save_score(name, score, total)
            print("\nYour result has been saved.")
        elif choice == '2':
            show_past_scores()
        elif choice == '3':
            print("Thank you for taking the quiz. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
main()