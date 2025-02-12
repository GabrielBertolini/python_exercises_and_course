# %%

sum = 0
entries_quantity = 4  # Counter of entries

for i in range(entries_quantity):  # Loop runs 4 times
    height = input("Enter the height: ")  # Indented properly inside loop
    height = float(height)  # Convert input to float
    sum += height  # Add to sum

print("Height sum:", sum)  # Print final sum