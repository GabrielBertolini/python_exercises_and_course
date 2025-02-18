# %%

file = "data.csv"

with open(file) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)
        
# %%
data = dict()

keys = lines[0].strip("\n").split(";")
for c in keys:
    data[c] = []

data
# %%

for l in lines[1:]:

    values=l.strip("\n").split(";")

    for i in range(len(keys)):

        data[keys[i]].append(values[i])

data
# %%

ages=[]
for i in data["age"]:
    ages.append(int(i))
ages

avg=sum(ages)/len(ages)
avg
# %%
