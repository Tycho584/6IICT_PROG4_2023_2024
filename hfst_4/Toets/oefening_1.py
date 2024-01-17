""" OEFENING 1 (   / 1.5)
Onderstaande code implementeert het spel hoger-lager.
Momenteel crasht dit spel alleen als de input van de gebruiker geen geheel getal is.

Het is aan jullie om ook exceptions te laten optreden (raisen) in andere gevallen.
    - Getal is kleiner dan 0 of hoger dan 100. 
    - Gebruiker geeft een getal op dat deze al heeft opgegeven (zie variabele gegokte_getallen)
    - Na 8 pogingen (wie is er zo slecht in hoger-lager?).
Gebruik hiervoor Custom Exceptions (je mag naam & uitleg zelf kiezen).

"""

import random

class TeLaagGetal(Exception):
    pass

class TeVeelPogingen(Exception):
    pass

class GetalAlIngegeven(Exception):
    pass

def start_hogerlager():
    # Verwelkom speler & leg spel uit.
    print("Welkom bij het spel hoger-lager. Probeer zo snel mogelijk het geheime getal te raden.")
    print(f"Dit is een getal tussen 0 en 100. Veel success!\n")

    # Bepaal geheim getal & zet wat variabelen klaar.
    geheim_getal = random.randint(0, 100)
    pogingen, gegokte_getallen = 0, []
    while True:
        try:
            # Vraag gebruiker om getal.
            gegokt_getal = int(input(f"Wat is het geheime getal (poging: {pogingen+1}): "))

            if gegokt_getal in gegokte_getallen:
                raise GetalAlIngegeven("Geeft u eens een nieuw getal in, zo wordt het wel een beetje saai.")

            if gegokt_getal < 0 or gegokt_getal > 100:
                raise TeLaagGetal("Geef een getal van 0 tot 100 in!!!")

            # Controleer of dit getal hoger/lager is dan geheim getal (en print dit).
            # Anders als het getal correct is, stop de while-loop.


            if   gegokt_getal < geheim_getal:
                print("Je zult wat hoger moeten gokken!")
            elif gegokt_getal > geheim_getal:
                print("Fout, zoek het wat lager!")
            else:
                break



            # Verhoog het aantal pogingen met 1 & voeg het gegokte getal toe aan een lijst.
            pogingen += 1
            gegokte_getallen.append(gegokt_getal)

            if pogingen > 7:
                raise TeVeelPogingen("Jij bent wel heel erg slecht in dit spel")

        except ValueError:
            print("Geef een geheel gatal in!!!")

    # Na getal te raden. Print wat regels...
    print(f"Goed zo! Het getal was inderdaad {gegokt_getal}")
    print(f"Je had {pogingen} nodig om het getal te raden.")




start_hogerlager()