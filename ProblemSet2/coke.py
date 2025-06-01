#Starting amount due
amount_due = 50

#Ask user to insert coing / Loop until user inputs enough coins / Check if valid coin used / Show user amount due
while amount_due > 0:
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        amount_due -= coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

#If user inputs excess coins this will give change
print(f"Change Owed: {abs(amount_due)}")