# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests, json

url = f"https://v2.jokeapi.dev/joke/Christmas?amount=3"
response_json = requests.get(url).json() # Haal JSON uit response.
with open("bericht_jokeAPI.json", "w") as fp:
    json.dump(response_json, fp)

# Bepaal of de grap uit 1 of 2 delen bestaat.
for aantal in range(3):
    if ("joke" in response_json):
        print(response_json["jokes"][aantal]["joke"])     # De grap
    else:
        print(response_json["jokes"][aantal]["setup"])    # De setup
        print(response_json["jokes"][aantal]["delivery"]) # De punchline
    print("-"*40)

