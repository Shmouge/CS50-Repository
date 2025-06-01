#Request user input time
def main():
    time = input("What time is it? ").strip()
    try:
        hour = convert(time)
    except ValueError:
        print("Invaild input.")
        return

#If this than, otherwise this, otherwise this
    if 7 <= hour <= 8:
        print("breakfast")
    elif 12 <= hour <= 13:
        print("lunch")
    elif 18 <= hour <= 19:
        print("dinner")

#Convert HH:MM
def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()