sample_messages = [
    "Congratulations! You've won a prize, click here to claim.",
    "Hi, can we meet tomorrow for the project update?",
    "Urgent! Your bank account has been compromised, verify now!",
    "Let's have lunch today.",
    "You have been selected for a free gift card."
]

with open("messages.txt", "w", encoding="utf-8") as f:
    for msg in sample_messages:
        f.write(msg + "\n")

print("Sample messages.txt file created!")
