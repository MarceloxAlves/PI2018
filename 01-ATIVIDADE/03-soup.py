import requests
from bs4 import BeautifulSoup

url =  input("Digite a URL: \n").strip()

response = requests.get( url );

content = response.text

soup  = BeautifulSoup(content,'html5lib')

print(soup.prettify())


