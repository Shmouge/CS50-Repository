#note: Ask the user for a height between 1 and 8
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        pass

#note: Loop from 1 to height, building each row
for i in range(1, height + 1):
    #note: Print spaces to right-align the pyramid, then hashes
    print(" " * (height - i) + "#" * i)