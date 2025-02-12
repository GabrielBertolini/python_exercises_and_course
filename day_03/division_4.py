# %%

# #which numbers are divisable by 4 in the [4-100] interval?

count=4
while count <=100:
    remainder=count%4
    if remainder==0:
        print(count)
    
    count +=1
