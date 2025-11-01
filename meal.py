#Request user input time
def main():
    time = input("What time is it? ").strip()
    hour = convert(time)

    if 7 <= hour <= 8:
        print("breakfast")
    elif 12 <= hour <= 13:
        print("lunch")
    elif 18 <= hour <= 19:
        print("dinner")

#Convert HH:MM
def convert(time):
    if ":" in time:
        hours, minutes = time.split(":")
        return int(hours) + int(minutes) / 60
    else:
        return float(time)

if __name__ == "__main__":
    main()