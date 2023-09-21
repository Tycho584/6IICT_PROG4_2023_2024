# Voer onderstaande code uit & bekijk het resultaat.
import requests, json

url = "https://v2.jokeapi.dev/joke/Any"
response = requests.get(url)
response_json = response.json()
print(response_json)
