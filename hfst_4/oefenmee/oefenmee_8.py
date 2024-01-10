import json

try:
    bestand_boodschappen = "6IICT_PROG4_2023_2024\hfst_4\oefenmee\oefenmee_8.json"

    with open(bestand_boodschappen, 'r') as file:
        boodschappen = json.load(file)

    fruit = input("Van welk fruit wil je de hoeveelheid weten: ")
    aantal = int(boodschappen[fruit])
    print(f"Er staan {aantal} {fruit} op de lijst.")

except FileNotFoundError:
    print("Controlleer het pad naar het bestand, want we kunnen het niet vinden")

except KeyError:
    print("De sleutel is niet gevonden, geef een fuit in dat al bestaat")

else:
    print(f"Er zijn nog {len(boodschappen) - 1} fruitsoorten in de boodschappen.")

finally:
    print("Bedankt om gebruik te maken van de boodschappen-app!")