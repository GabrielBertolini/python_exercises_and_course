import requests

cep = input("Enter your CEP:" )

url = "https://viacep.com.br/ws/{cep}/json/"

answer = requests.get(url.format(cep=cep))

data = dict()
if answer.status_code == 200:
    data = answer.json()

for key, value in data.items():
    print(key, "->", value)