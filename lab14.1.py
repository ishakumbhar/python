
print("=" * 50)
print("SURVEY ANALYTICS TOOL")
print("=" * 50)

categories = ["Mobile", "Laptop", "Tablet", "Smartwatch"]

votes = [
    "Mobile",
    "Laptop",
    "Mobile",
    "Tablet",
    "Laptop",
    "Mobile",
    "Smartwatch",
    "Tablet",
    "Mobile",
    "Laptop"
]

vote_count = {}

for category in categories:
    vote_count[category] = 0

for vote in votes:
    if vote in vote_count:
        vote_count[vote] = vote_count[vote] + 1

print("\n---------- SURVEY RESULTS ----------")

for category in vote_count:
    print(category, "->", vote_count[category], "votes")

winner = categories[0]

for category in categories:
    if vote_count[category] > vote_count[winner]:
        winner = category

print("\n---------- WINNER ----------")
print("Winning Product Category:", winner)
print("Number of Votes:", vote_count[winner])
