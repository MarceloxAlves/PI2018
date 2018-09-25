import requests


def pesquisa_href( conteudo ):
    ponteiro = 0
    chave = "href="
    link = False
    url = ''
    aspa = False
    lista = list()
    link_valido = False
    for a in conteudo:
        if( not aspa ):
            if( a == chave[ponteiro] ):
                if( ponteiro == len(chave)-1 ):
                    print(a)
                    link = True
                    ponteiro = 0
                else:
                    ponteiro += 1
            else:
                ponteiro = 0
        if( link and not aspa ):
            if(ord(a) == 34 or ord(a) == 39):
                aspa = True
                link_valido = True
                continue
        if aspa:
            if (ord(a) == 34 or ord(a) == 39):
                aspa = False
                lista.append(url)
                link = False
                url = ''
            else:
                if(link_valido):
                    if a != "h":
                        aspa = False
                        link = False
                        url = ''
                        continue
                    link_valido = False
                url += a
    return lista


url =  input("Digite a URL: \n").strip()

response = requests.get( url );

content = response.text

print(pesquisa_href(content))


