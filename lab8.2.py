feedback = input("Enter Feedback: ")

target_words = ["bad", "stupid", "idiot"]

for word in target_words:
    feedback = feedback.replace(word, "****")

print("Filtered Feedback:", feedback)