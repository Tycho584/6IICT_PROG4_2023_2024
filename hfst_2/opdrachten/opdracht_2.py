# Start deze opdracht met onderstaande code.

import json, requests # Benodigde modules

"""	STAP 1: endpoint klaarmaken voor versturen request """
# Geef tweeletter-code van land (https://www.iban.com/country-codes)
land = input("Geef tweeletter-code van land (Belgie = BE): ")
# Geef stad:
stad = input(f"Geef stad (in het Engels): ")
# Geef API-key:
API_key = "7361b1cc0fec5ea1eaac40197d453745"

# Stel de url  op, waarmee we JSON-data kunnen afhalen van openweathermap.org
url = f"https://api.openweathermap.org/data/2.5/forecast?q={stad},{land}&appid={API_key}"



""" STAP 2: JSON-data via request afhalen van openweathermap.org endpoint """
# Roep weerdata op via endpoint (= url).
response_json = requests.get(url).json()

with open("bericht_openweather.json", "w") as fp:
    json.dump(response_json, fp)



""" STAP 3: Haal bewolkingsinfo uit JSON-data """

# Zowel dag als uur (is samen te vinden in de JSON-data!)
tijd_vandaag    = response_json["list"][0]["weather"]["discription"]
tijd_morgen     = response_json["list"][8]["weather"]["discription"]
tijd_overmorgen = response_json["list"][16]["weather"]["discription"]

# Zowel hoofd- als sub-categorie van bewolking in deze variabele zetten (zijn apart te vinden in de JSON-data).
bewolking_vandaag    = "VUL AAN"
bewolking_morgen     = "VUL AAN"
bewolking_overmorgen = "VUL AAN"



""" STAP 4: Print bewolkingsinfo """

# Dit moet de laatste regel zijn. Zonder deze zal de exe meteen sluiten.
input("Druk op enter om de app te sluiten.")