
#Prompt the user for camelCase name
camel = input("camelCase: ")

#Prepare empty string for snake_case result
snake = ""

#Loop each character in user input
for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char

#nOutput in snake_case
print("snake_case:", snake)