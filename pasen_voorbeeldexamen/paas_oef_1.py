""" OEFENING 1: (  / 5)

!!! OPGELET: Je mag de huidige code niet wijzigen. Je mag enkel code toevoegen. !!!

Onderstaande code gebruikt een API om een willekeurig woord te genereren.
Dit woord zal later gebruikt worden in een raad-spel (hoort niet bij deze oefening).
Enkel indien het woord correct geladen is, zal dit spel starten (zie if-else).
"""

# try:
#     import requests

#     woord_geladen = False
#     moeilijkheid = input("Woord van hoeveel letters: ")
#     API = f"https://random-word-api.herokuapp.com/word?length={moeilijkheid}"
#     woord = requests.get(API).json()[0]
#     print(woord)

# except KeyboardInterrupt:
#     print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     print("De gebruiker heeft op de verboden knoppencombinatie geduwd (ctrl + c)!!!")
#     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# except IndexError:
#     print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     print("De gebruiker heeft een ongeldig getal ingegeven!")
#     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# if woord_geladen:
#     print("START HET SPEL!")
# else:
#     print("Er ging iets mis. Kon spel niet starten.")

""" NIVEAU 1: (  / 2)
Tijdens de functie input (voor moeilijkheid), kunnen 2 fouten onstaan:
    - De speler onderbreekt de input via CTRL+C.
    - De speler geeft een ongeldige input in (kommagetal, negatief getal).

We willen niet dat de speler in dit geval foutmeldingen ziet. Breng daarom een try-except aan.
Vang specifiek bovenstaande foutmeldingen op, en leg via een print uit wat er mis ging. 
Neem de if-else niet op in deze try-except. 

VOORBEELD:
    Woord van hoeveel letters: 4
    *ER GAATS NIET FOUT.*

    Woord van hoeveel letters: *Druk op CTRL+C*
    Speler heeft programma onderbroken.

    Woord van hoeveel letters: -7
    Speler heeft verkeerde input gegeven.

"""


""" NIVEAU 2: (  / 2)
woord_geladen is tot nog toe altijd False. Dit zorgt ervoor dat de code onder 
de else altijd print. Zorg ervoor dat woord_geladen als waarde True krijgt, 
als er geen exceptions optreden in de try-except.

VOORBEELD:
    Woord van hoeveel letters: -7
    Speler heeft verkeerde input gegeven.
    Er ging iets mis. Kon spel niet starten.

    Woord van hoeveel letters: 4
    START HET SPEL!

"""
# try:
#     import requests

#     woord_geladen = False
#     moeilijkheid = input("Woord van hoeveel letters: ")
#     API = f"https://random-word-api.herokuapp.com/word?length={moeilijkheid}"
#     woord = requests.get(API).json()[0]
#     print(woord)

# except KeyboardInterrupt:
#     print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     print("De gebruiker heeft op de verboden knoppencombinatie geduwd (ctrl + c)!!!")
#     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# except IndexError:
#     print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     print("De gebruiker heeft een ongeldig getal ingegeven!")
#     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# else:
#     woord_geladen = True

# if woord_geladen:
#     print("START HET SPEL!")
# else:
#     print("Er ging iets mis. Kon spel niet starten.")

""" NIVEAU 3: (  / 1)
Momenteel krijgt de speler geen feedback over wat verkeerd is aan zijn input.
Voeg code toe om hem specifiek voor volgende fout te waarschuwen.
    - De ingegeven input is negatief.

Maak hiervoor een CustomExceptions aan. Kies zelf de naam en de gegeven uitleg.
    Tip! Raise deze CustomException wanneer noodzakelijk,
         en vang ze vervolgens op in de try-except.

VOORBEELD:
    Woord van hoeveel letters: -7
    Speler heeft een negatief getal opgegeven.
    Er ging iets mis. Kon spel niet starten.

"""
class NegativeError(Exception):
    pass
class KommagetalError(Exception):
    pass

try:
    import requests

    woord_geladen = False
    moeilijkheid = input("Woord van hoeveel letters: ")
    API = f"https://random-word-api.herokuapp.com/word?length={moeilijkheid}"
    woord = requests.get(API).json()[0]
    print(woord)

except KeyboardInterrupt:
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("De gebruiker heeft op de verboden knoppencombinatie geduwd (ctrl + c)!!!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

except IndexError:
        raise NegativeError(print("NEGATIEF!!!"))
except requests.exceptions.JSONDecodeError:
        raise KommagetalError(print("KOMMAGETAL!!"))

else:
    woord_geladen = True

if woord_geladen:
    print("START HET SPEL!")
else:
    print("Er ging iets mis. Kon spel niet starten.")