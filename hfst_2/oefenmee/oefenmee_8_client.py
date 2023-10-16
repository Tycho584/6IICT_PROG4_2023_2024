"Dit bestand helpt je met het testen van oefenmee 8, niveau 2."

import requests

url_1 = "http://127.0.0.1:5000/toevoegen_todo?taak=winkelen"
url_2 = "http://127.0.0.1:5000/toevoegen_todo"

print(requests.post(url_1).json())
print(requests.post(url_2).json())