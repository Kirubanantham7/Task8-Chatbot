import random
from datetime import datetime

# List of random jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What did one wall say to the other? 'I’ll meet you at the corner!'",
    "Why did the math book look sad? Because it had too many problems.",
    "Why don’t eggs tell jokes? Because they’d crack each other up.",
    "I told my computer I needed a break, and now it won’t stop sending me beach photos."
]

print("Lexa: Hey there! I'm your friend Lexa . Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Lexa: Hello, my friend! How can I brighten your day?")
    elif "how are you" in user_input:
        print("Lexa: I'm doing great, especially now that you're here. How about you?")
    elif "your name" in user_input:
        print("Lexa: I'm Lexa your friendly Python chatbot.")
    elif "help" in user_input:
        print("Lexa: I can chat with you, tell jokes, give the time and date, or just be a good friend.")
    elif "joke" in user_input:
        print(f"Lexa: {random.choice(jokes)}")
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Lexa: The current time is {current_time}.")
    elif "date" in user_input:
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Lexa: Today's date is {current_date}.")
    elif "friend" in user_input or "talk" in user_input:
        print("Lexa: I'm always here to talk, like any good friend would be!")
    elif user_input == "bye":
        print("Lexa: See you soon! Take care, my friend.")
        break
    else:
        print("Lexa: Hmm, I'm not sure what to say. But I'm here for you!")
