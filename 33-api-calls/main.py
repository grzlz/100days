import requests

response = requests.get(url="https://api.kanye.rest/")
print(response.json().get("quote"))