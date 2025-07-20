#twttr.py 2.0 - modified from original to expose a shorten function for test import

#Shorten function
def shorten(word):
    """
    Return word with all vowels (A, E, I, O, and U), upper- or lowercase, removed.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for ch in word:
        if ch not in vowels:
            result += ch
    return result

#Main now as function
def main():
    text = input("Input: ")
    print(shorten(text))


if __name__ == "__main__":
    main()