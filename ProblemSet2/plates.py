#Main
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Check user input
def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    #Additional criteria for #s in user input
    number_found = False
    for i, c in enumerate(s):
        if c.isdigit():
            if not number_found:
                number_found = True
                if c == '0':
                    return False
            else:
                continue 
        elif number_found:
            return False

    return True

main()