total_balance=0

while True:
    balance=input("Enter you balance: ")
    if balance=="":
        break

    total_balance+=float(balance)

print("Total balance is: ",total_balance)