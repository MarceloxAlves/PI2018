import requests

TOKEN  = "TOKEN"
header = {
"Content-Type": "application/json",
"Authorization":"Bearer " + TOKEN
}

payload = {

}

url = "https://api.sandbox.paypal.com/v1/payments/payment";
response = requests.get(url,header=header).json()

print(response)
