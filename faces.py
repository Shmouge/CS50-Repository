#Ask the user for input with text-based emoji
message = input("Type something with a face: ")

#Replace :) with 😊 and :( with 🙁
message = message.replace(":)", "😊").replace(":(", "🙁")

#Output the updated message with emojis
print(message)