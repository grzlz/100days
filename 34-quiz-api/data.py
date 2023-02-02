import requests 

url_parameters = {"amount": "10", "type": "boolean"}
r = requests.get("https://opentdb.com/api.php", params=url_parameters)

question_data = r.json()["results"]
