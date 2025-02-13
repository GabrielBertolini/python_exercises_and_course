
ages = [] 

while True:
    age = input("Enter an age: ") 

    if age == "":  
        break

    ages.append(int(age))

print(ages)

mean=sum(ages)/len(ages)
min=min(ages)
max=max(ages)
quantity=len(ages)

print("MEAN: ",mean)
print("MIN: ",min)
print("MAX: ",max)
print("QUANTITY: ",quantity)


print("mean: ",mean)
print("min: ",min)
print("max :",max)
print("quantity :", quantity)
