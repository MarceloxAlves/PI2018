import hashlib
import requests

PUBLIC_KEY = "w7gaavla35y0wnpwg8fofw8o66t3vmhx"
PRIVATE_KEY = "PRIVATE_KEY"

prepare = PRIVATE_KEY + "accesspublicactionissuu.documents.listapiKey" + PUBLIC_KEY + "formatjsonresponseParamstitle,description"
h = hashlib.md5(prepare.encode())
payload = {
    "apiKey": PUBLIC_KEY,
    "access": "public",
    "responseParams": "title,description",
    "format": "json",
    "signature": h.hexdigest()
}
url = "http://api.issuu.com/1_0?action=issuu.documents.list";
response = requests.get(url, payload).json()

print(response)
