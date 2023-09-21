# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests

url = "https://v2.jokeapi.dev/joke/Christmas"
response_json = requests.get(url).json() # Haal JSON uit response.

# Bepaal of de grap uit 1 of 2 delen bestaat.
if ("joke" in response_json):
    print(response_json["joke"])     # De grap
else:
    print(response_json["setup"])    # De setup
    print(response_json["delivery"]) # De punchline

