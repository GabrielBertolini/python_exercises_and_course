
# %%
file_name = "story.txt"

with open(file_name) as open_file:
        content=open_file.read()

print(content)

# %%
open_file = open(file_name)

content=open_file.read()

print(content)

open_file.close
# %%
