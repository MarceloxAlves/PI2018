import requests

def procura_ultimo_ponto(url):
    indice = 0
    pos = -1
    while indice < len(url):
        if url[indice] == ".":
            pos  = indice
        indice = indice + 1
    return pos

url =  input("Digite a URL da Imagem: \n").strip()
response = requests.get(url, stream = True);
extension = url[procura_ultimo_ponto(url):]
if response.status_code == 200:
    with open(input("Nome da Imagem: \n")+ extension, 'wb') as fd:
        for chunk in response.iter_content():
            fd.write(chunk)
    print("Download concluído...")

