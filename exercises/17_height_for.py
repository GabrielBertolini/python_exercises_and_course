# %%

sum = 0
quantity_entries = 4  # Counter of entries

for i in range(quantity_entries):  # Loop runs 4 times
    height = input("Enter the height: ")  # Indented properly inside loop
    height = float(height)  # Convert input to float
    sum += height  # Add to sum

print("Height sum:", sum)  # Print final sum