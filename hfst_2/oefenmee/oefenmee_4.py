# Maak een eigen JSON-bestand aan met behulp van onderstaande code.
import requests, json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()

with open("bericht_adviceslip.json","w") as file:
    json.dump(response_json, file)
