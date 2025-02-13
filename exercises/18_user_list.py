
# %%
list=[1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

number=input("Type a number :")
number=int(number)

counter=0
for i in list:
    if i == number:
        counter+=1

print("Quantity of",number,":",counter)


# %%
