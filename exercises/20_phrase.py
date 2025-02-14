data={ }

while True:
    phrase = input("Enter with a phrase: ")
    
    if phrase == "":  
        break  

    if phrase not in data:  
        data[phrase] = 1  
    else:
        data[phrase] += 1

for i,j in data.items():
    print(i,"->",j)

#for i,j in data.items():
#   print(i,"->",data[i])

items=list(data.items())
items.sort(key=lambda x: x[-1],reverse=True)
items
# %%
