import requests
from urllib.parse import urlencode


TOKEN = "TOKEN"
KEY =  "KEY"

url = "https://api.trello.com/1/tokens/"+TOKEN
AUTH = {
    "key": KEY,
    "token": TOKEN
}
response = requests.get(url, AUTH).json()
id_member = response['idMember']


def list_board(id):
    url = "https://api.trello.com/1/members/" + id + "/boards"
    response = requests.get(url, AUTH).json()
    for board in response:
        print(board["id"]+ " - " + board["name"])


def create_board():
    url = "https://api.trello.com/1/boards/"
    payload = {}
    object = {
        "name": input("Type a name: ")
    }
    payload.update(object)
    payload.update(AUTH)
    response = requests.post(url, payload)
    if (response.status_code == 200):
        print("Board criado com sucesso")
    else:
        print("Erro ao criar")


def delete_board():
    url = "https://api.trello.com/1/boards/"+ input("Paste here id of board: ") +"?"+ urlencode(AUTH)
    response = requests.delete(url)
    if (response.status_code == 200):
        print("Board deletado com sucesso")
    else:
        print("Erro ao deletar")

rodando = True

while (rodando):
    op = int(input("1 - List Boards\n2 - Create Board\n3 - Delete Board\n>>"))
    if op == 1:
        list_board(id_member)
    if op == 2:
        create_board()
    if op == 3:
        delete_board()
    if op == 4:
        rodando  = False
        print("\n\n______( 0.0 )________\n\n")
