""" OEFENING 2 (   / 3.5)
In onderstaande code wordt gevraagd om een kluis te kiezen (zie JSON).
De code print de inhoud van deze kluis, en vraagt vervolgens om een voorwerp
toe te voegen aan de kluis & een voorwerp uit de kluis te verwijderen.
Tenslotte schrijft het de wijzigingen terug weg naar het JSON-bestand.

Via de while True blijft bovenstaande herhalen.
Dit tot de gebruiker "STOP" ingeeft, in plaats van een kluis te kiezen.


NIVEAU 1:

De code kan op verschillende wijzen fout gaan. Hiervoor is reeds een try-except
aangebracht. Deze simpele except geeft echter niet aan wat het exacte probleem is.
Pas de try-except aan door specifieke exceptions toe te voegen. 

Er moeten specifieke exceptions zijn voor volgende situaties:
    - JSON-bestand niet gevonden: print uitleg over probleem + stop programma (via exit).
    - Opgegeven kluis bestaat niet: print uitleg over probleem.
    - Te verwijderen voorwerp bestaat niet: print uitleg over probleem.

Enkel indien het JSON-bestand niet gevonden is, moet het programma stoppen.
In alle andere gevallen, gaat de while-loop dus gewoon verder.


NIVEAU 2:

Lukt het om de code ZONDER fouten te doorlopen. Print dan:
"De kluis is met succes gewijzigd!"


NIVEAU 3:

De nieuwe inhoud van de kluizen moet ALTIJD weggeschreven worden.
Dus ook als er midden in het programma een fout ontstaat, of de gebruiker
via CTRL+C expres het programma stopt.

Je kan dit testen door een voorwerp toe te voegen & vervolgens CTRL+C in te drukken.
Ondanks het crashen moet het toegevoegde voorwerp nog steeds in de JSON staan.

"""

import json

# Pad naar JSON-bestand & lege dict klaarzetten voor inhoud van kluisjes.
pad = "hfst_4\Toets\oef2_kluizen.json"
kluizen = {}

while True:
    try:
        # Haal inhoud van kluizen op uit JSON-bestand.
        with open(pad, "r") as fp:
            kluizen = json.load(fp)

        # Vraag gebruiker om een kluis te kiezen
        # Het programma stopt wanneer de gebruiker STOP ingeeft, in plaats van een kluis.
        nummer_kluis = input("Welke kluis openen: ")
        if nummer_kluis.upper() == "STOP":
            break

        # Print inhoud van de gekozen kluis.
        print(f"In deze kluis zitten volgende zaken...")
        for voorwerp in kluizen[nummer_kluis]:
            print(f"    - {voorwerp}")

        # Vraag gebruiker om voorwerp toe te voegen aan kluis.
        voorwerp = input("Voorwerp toevoegen aan kluis: ")
        if voorwerp.strip() != "":
            kluizen[nummer_kluis].append(voorwerp)

        # Vraag gebruiker om voorwerp uit kluis te halen.
        voorwerp = input("Voorwerp verwijderen uit kluis: ")
        if voorwerp.strip() != "":
            kluizen[nummer_kluis].remove(voorwerp)

    except FileNotFoundError:
        print("Het bestand is niet gevonden!!!")

    except ValueError:
        print("Dit voorwerp zit niet in de kluis, ik kan ook niet toveren hé, gebruik je ogen eens.")

    except KeyError:
        print("Dit kluisje bestaat niet, Lees de nummers van de kluis eens, als er nog steeds een probleem voordoet")
        print("bel dan naar meneer Clijsters of Colson.")

    else:
        print("Kluisinhoud is met succes gewijzigd")

    finally:
        with open(pad, "w") as fp:
            kluizen = json.dump(kluizen, fp)