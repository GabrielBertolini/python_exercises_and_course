text = """Choose your water:
(1) Still Water
(2) Sparkling Water
"""

option = input(text)  # Remove any accidental spaces or newlines

item_value=0
if option == "1":
    item_value = 1.5  # Still water
elif option == "2":
    item_value = 2.5  # Sparkling water

if item_value==0:
    print("choose either 1 or 2")
else:
    quantity=input("How many bottles?")
    quantity=int(quantity)
    total_value=item_value*quantity
    print("Your bill is: $",total_value)

