#User input
text = input("Input: ")

#Vowels to exclude
vowels = "aeiouAEIOU"

#Empty result string
shortened = ""

#Loop through character inputs
for char in text:
    if char not in vowels:
        shortened += char

#Print result to user
print("Output:", shortened)