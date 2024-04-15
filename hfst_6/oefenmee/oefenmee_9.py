# Bepaal het aantal bestanden in een map (en alle submappen).
import os
def doorzoek_map(filePath):
    grootte = 0
    teller = 0
    items = os.listdir(filePath)  # Zet de inhoud van de map in een lijst.
    for item in items: # Overloop ieder item.
        item_pad = os.path.join(filePath, item)  # Haal pad van item op.

        if os.path.isfile(item_pad):        # Is item een bestand?
            # print(f"{item} is een bestand.")
            grootte += os.path.getsize(item_pad) / (1024**2)    
            # print(grootte)
            teller += 1
        elif os.path.isdir(item_pad):       # Is item een map?
            # print(f"{item} is een map.")
            teller += doorzoek_map(item_pad)[0]
            grootte += doorzoek_map(item_pad)[1]

    return teller, grootte

# " Opgelet! uitkomsten geven aantal bestanden aan. Mappen zelf zijn niet meegeteld. "
print( doorzoek_map("hfst_1") )    # 40 
print( doorzoek_map("hfst_5") )    # 553 
print( doorzoek_map("hfst_6") )    # 43
