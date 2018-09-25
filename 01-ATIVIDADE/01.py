import requests

response = requests.get(input("digite uma URL\n"));
print("Status Code: %s \n"  % response.status_code)
print("Cabeçalhos: %s \n" % response.headers)
print("Tamanho Resposta: %s" % len(response.content))