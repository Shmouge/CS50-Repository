#Display the great question
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

#Process and output
if answer in ["42", "forty two", "forty-two"]:
    print("Yes")
else:
    print("No")