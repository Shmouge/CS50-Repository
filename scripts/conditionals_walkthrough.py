# CS50 Python Lecture 1 - Conditionals Summary Script
# This script will walk you through core conditional concepts in Python

# ---------------------------------------
# DAY 1: Basic Conditionals and Comparisons
# ---------------------------------------

# Let's start by getting two numbers from the user and comparing them

x = int(input("What's x? "))
y = int(input("What's y? "))

# Basic if statement
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# ---------------------------------------
# DAY 2: Boolean Logic and Pythonic Refinement
# ---------------------------------------

# Now, let's use Boolean operators: and, or, not

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Let's also use 'or' for a name-based logic

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("You're in Gryffindor.")
elif name == "Draco":
    print("You're in Slytherin.")
else:
    print("Who?")

# ---------------------------------------
# DAY 3: Functions and Boolean Return Values
# ---------------------------------------

# Define a function that checks if a number is even
def is_even(n):
    return n % 2 == 0  # returns True if even, False otherwise

num = int(input("Enter a number to check even/odd: "))
if is_even(num):
    print("Even")
else:
    print("Odd")

# ---------------------------------------
# DAY 4: Match Statements and Clean Code
# ---------------------------------------

# The match statement is a cleaner alternative to long if-elif chains

person = input("Enter your name for house sorting: ")

match person:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# ---------------------------------------
# Challenge (Optional)
# Create your own function that returns "Pass" if score >= 60, else "Fail"
# Use that function inside a conditional.
# ---------------------------------------
