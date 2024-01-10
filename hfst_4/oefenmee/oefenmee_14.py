" Maak oefen mee 14 op basis van de uitleg in OneNote. "

try:
    waardeTeller = float(input("Geef hier een getal op voor de teller: "))
    waardeNoemer = float(input("Geef hier een getal op voor de noemer: "))

    if waardeTeller < 0 or waardeNoemer < 0:
        raise ValueError ("Een van de getallen is negatief, dat vinden wij niet zo leuk!!!")
    
    if waardeTeller > waardeNoemer:
        raise ValueError ("De teller moet kleiner zijn dan de noemer want de tank kan niet overvol zijn (check je tank)!!!")

    uitkomst = round(float(waardeTeller / waardeNoemer),2)
    print(uitkomst)
    

except ValueError:
    print("GEEF EEN GETAL IN!!!")

except ZeroDivisionError:
    print("NIET DELEN DOOR 0!!!")

finally:
    print("Bedankt voor het cheken van je tank.")

