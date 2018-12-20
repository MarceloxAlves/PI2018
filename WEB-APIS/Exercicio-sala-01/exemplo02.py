import requests
cep = '64000070'
url = "https://viacep.com.br/ws/%s/json/" % cep
response = requests.get(url).json()
# print(response)
print("Logradouro: %s \n Bairro: %s \n"
      "Localidade: %s \n UF: %s" %
       (response['logradouro'],
       response['bairro'],
       response['localidade'], response['uf']))