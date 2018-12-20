import requests

TOKEN  = "ACCESS TOKEN"
header = {
"Content-Type": "application/json",
"Authorization":"Bearer <Access Token>"
}

body = {

}

url = "https://api.sandbox.paypal.com/v1/payments/payout";
response = requests.get(url,data=body, header=header).json()

print(response)
