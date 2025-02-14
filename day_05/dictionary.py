# %%

#pair of keys/value
# %%

data_gabriel= {"Name":"Gabriel",
               "Surname": "Bertolini",
               "sons":False
               ,"Graduation":["statistics","bigdata data science"],
               "positions":[
                {"name": "ds jr.","company":"google"},
                {"name": "ds mid.","company":"microsoft"},
                {"name": "ds senior","company":"netflix"},
                {"name": "head of ds","company":"NASA"},
               ]}


# %%

print(data_gabriel)
data_gabriel["Graduation"][-1]
data_gabriel["positions"][-1]["company"]

# %%

data_gabriel["marital status"]="single"

print(data_gabriel)


# %%

print("keys:",data_gabriel.keys())

print("values:",data_gabriel.values())

print("items:",data_gabriel.items())
# %%
for key, value in data_gabriel.items():
    print(key, "->", value)



# %%
