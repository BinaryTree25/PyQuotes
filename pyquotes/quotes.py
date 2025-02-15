import random

# List of programming-related quotes
QUOTES = [
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
    "Simplicity is the soul of efficiency. - Austin Freeman",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Optimism is an occupational hazard of programming: feedback is the treatment. - Kent Beck",
    "Make it work, make it right, make it fast. - Kent Beck",
    "The best way to predict the future is to invent it. - Alan Kay",
    "Programming isn't about what you know; it's about what you can figure out. - Chris Pine",
    "The function of good software is to make the complex appear simple. - Grady Booch",
]

def get():
    """Returns a random programming quote."""
    return random.choice(QUOTES)