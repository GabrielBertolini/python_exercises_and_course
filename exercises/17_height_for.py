# %%

sum=0
quantity_entries=4 #counter of entries

for i in range(quantity_entries)
height =input("Enter the height: ")
height=float(height)
sum += height
quantity_entries -=1

print("Height sum: ",sum)