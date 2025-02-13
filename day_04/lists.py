# %%

ages=[10,20,30,40,50,60]
print(ages)


gabriel=["Gabriel", "Bertolini",22,1,"Single",22100.30]

# %%
type(gabriel)
# %%

print(gabriel[2])
print(gabriel[0])

# %%
total_sum=sum(ages)

print("Sum of the ages is",total_sum)
print("quantity of ages is",len(ages))
print("Average of the ages is",(total_sum)/len(ages))
print("Smallest age is",min(ages))
print("Biggest age is",max(ages))

# %%

gabriel = ["Gabriel Bertolini", 22, True,
 "Single", ["Ana", "Maria", "Daniela"]]

print("Size of Gabriel's list:", len(gabriel))
print(gabriel[4]) 
print(gabriel[4][1])  

# %%

gabriel = ["Gabriel Bertolini", 
           22, True, "Single",
          ["intern","ds jr","ds mid","ds sr","head"],
          [2000,4000,4550,6500,1000],
          ["Ana", "Maria", "Daniela"]]
           

print(gabriel[6][0])

exs=gabriel[6]
first_exs=exs[0]
print(first_exs)

# %%
size=len(gabriel)
pos=size-1
gabriel[pos][0]

exs=gabriel[pos]
gabriel[pos][len(exs)-1]

gabriel[-1][-2]

# %%

gabriel[0:4]
# %%

print(gabriel[4][3:5])
#gabriel[start:stop]
# %%

#gabriel[start:stop]
gabriel[4][-2:]
gabriel[4][3:] #mesma coisa


# %%

income=gabriel[5]
income[::-1]
income[::2]
 
#gabriel[start:stop:stop]
# %%
