sum=0
entries_quantity=4 #counter of entries

while entries_quantity >0:
    height =input("Enter the height: ")
    height=float(height)
    sum += height
    entries_quantity -=1

print("Height sum: ",sum)