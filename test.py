import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/ct")
#input()
#response = requests.post(BASE + "helloworld/gre", {"name": "gre", "year":10})

print(response.json())