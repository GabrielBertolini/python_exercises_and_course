
# %%
import requests #requests from web
import json # Enables reading, writing, and manipulating JSON data (lists/dictionaries)
from tqdm import tqdm
import pandas as pd

cep=[
    "90620130",
    "99709464",
    "90010150",
    "88190000",
    "90810240",
    "91509900",
]


url="https://viacep.com.br/ws/{cep}/json/"

answer=requests.get(url)
data=[]
for i in tqdm(cep):
    answer=requests.get(url.format(cep=i))
    if answer.status_code==200:
        data.append(answer.json())
data
# %%
dataset=pd.DataFrame(data)
dataset.to_csv("cep.csv",sep=";")

# %%
dataset_test=pd.DataFrame(data)
dataset_test

# %%
print(data)
with open("day_08/cep.json","w",encoding='utf-8') as open_file:
    json.dump(data,open_file,ensure_ascii=False,indent=4)



# %%
