text = """Choose your water:
(1) Still Water
(2) Sparkling Water
"""

option = input(text)  # Waits for user input after showing the prompt

bill = 0  # Default value

if option == "1":
    bill = 1.5  # Still water
elif option == "2":
    bill = 2.5  # Sparkling water

if bill == 0:
    print("Please choose either 1 or 2.")
else:
    print(f"Your total is: ${bill:.2f}")