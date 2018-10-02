import requests
import requests_cache
from bs4 import BeautifulSoup
import re
from flask import Flask, render_template, request, json
app = Flask(__name__)
requests_cache.install_cache(cache_name='buscapp_cache')

root = "http://ifpi.edu.br"
pesquisado = list()
resultados = list()
super_nivel = 3

def busca(keyword, content):
    body = content.body
    for script in body(["script","style"]):
        script.decompose()
    resultado = re.findall('\w*.{0,10}' + keyword + '.{0,30}\w*', body.text, re.IGNORECASE)
    return  resultado


def get_links(urls, keyword, cm):
    camada  = list()
    for url in urls:
        try:
            if(url in pesquisado):
                continue
            response = requests.get(url, timeout=0.1);
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            print(url)
            resultado = busca(keyword, soup)
            if resultado:
                resultados.append({"url": url, "result": resultado[0], "camada": cm})
            links = soup.body.find_all('a')
            for link in links:
                url1 = link.get('href')
                if (url1 != None and len(url1) > 10 and url1[0] == "h"):
                    if url1 not in camada and camada not in pesquisado:
                        camada.append(url1)
            pesquisado.append(url)
        except Exception as ex:
            print("Deu erro %s" % ex.args)
            pesquisado.append(url)
            continue

    return camada

def findSearch(url, nivel, keyword):
    print("Buacando nivel %s" % nivel)
    if nivel == 0:
        return url
    return findSearch(get_links(url,keyword, super_nivel-nivel), nivel-1, keyword)


@app.route("/")
def main():
    return render_template('./index.html')

@app.route("/buscar", methods=['POST'])
def buscar():
    resultados.clear()
    pesquisado.clear()
    keyword = request.form['busca']
    findSearch([root], 3, keyword)
    return json.dumps(resultados)


def debug():
    while True:
        resultados.clear()
        pesquisado.clear()
        findSearch([root], super_nivel, input("Digite uma palavra:\n"))
        print(resultados)


if __name__ == "__main__":
    #debug()
    app.run()

