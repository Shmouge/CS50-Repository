#Get bill total from user
def get_bill_total() -> float:
    return float(input("Bill total: ").strip())

#Get the tip % from user
def get_tip_percent() -> float:
    return float(input("Tip Percent: ").strip()) / 100

#Tip calculation
def calculate_tip(bill: float, percent: float) -> float:
    return bill * percent

#Answer
def display_tip(tip: float) -> None:
    print(f"${tip:.2f}")

#Main flow/control
def main() -> None:
    bill = get_bill_total()
    percent = get_tip_percent()
    tip = calculate_tip(bill, percent)
    display_tip(tip)

#Only run file as script
if __name__ == "__main__":
    main()