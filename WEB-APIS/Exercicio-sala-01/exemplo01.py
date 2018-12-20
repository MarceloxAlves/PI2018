import requests
cep = '64000070'
url = "https://viacep.com.br/ws/{cep}/json/"
url = url.format(cep=cep)
response = requests.get(url).json()
print(response)