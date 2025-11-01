#Ask for user greeting
greeting = input("Greeting: ").strip().lower()

#Process for payout based on user input
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")