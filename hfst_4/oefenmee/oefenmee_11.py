" Maak oefen mee 11 op basis van de uitleg in OneNote. "
ingegevenGetal = int(input("Geef een getal van 1 tot 10: "))

def verdubbelen(getal):
    if getal >= 1 and getal <= 10:
        getal = getal * 2
        print(getal)
        return getal
    raise ValueError ("Het getal moet liggen tussen 1 en 10")

verdubbelen(ingegevenGetal)