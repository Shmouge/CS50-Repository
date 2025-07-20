#note: Outer loop runs 3 times (rows)
for i in range(3):
    #note: Inner loop prints 3 '#' characters on the same line (columns)
    for j in range(3):
        print("#", end="")  #note: end="" prevents newline after each print
    print()  #note: prints a newline after each row