"""
In onderstaande app moet de functie toon_resultaat nog gemaakt worden.
Vul deze aan op basis van de instructies in de functie.

Voorbeelden van de uiteindelijke werking zijn te vinden bij oefen mee 15.
"""

import tkinter as tk

# 2 getallen en resultaat (vul in vooraleer app start)
getal_1 = int(input("Getal 1: "))
getal_2 = int(input("Getal 2: "))
resultaat = 0

# Toont het resultaat in het Label label_result.
def toon_resultaat():
    """ TODO:
    Deze functie is gelinkt aan de Button knop.

    NIVEAU 1
    Het drukken op de knop moet de waarde van globale variabele resultaat aanpassen.
    Deze moet de som van getal_1 & getal_2 als nieuwe waarde krijgen.

    Pas vervolgens ook de inhoud van Label label_result aan.
    Update hierin de waarde van variabele resultaat.
        Tip! gebruik .config() om de inhoud van label_result aan te passen.

    Voorbeelden zijn te vinden in OneNote.
    
    NIVEAU 2
    Voor het voorgaande niveau was het sleutelwoord global eigenlijk niet nodig. 
    Laten we dit aanpassen. Iedere keer dat je op de knop duwt, moet de som van de 2 getallen 
    toegevoegd worden aan de huidige waarde van resultaat.

    Als voorbeeld met getal_1 = 3 & getal_2 = 4.
        >>> 1x klikken: resultaat = 7
        >>> 2x klikken: resultaat = 14
        >>> 5x klikken: resultaat = 35
    Extra voorbeelden zijn te vinden in OneNote.
        
    """

# Open de app.
app = tk.Tk()

# Labels van getallen maken & plaatsen.
label = tk.Label(master=app, text="De twee getallen zijn:", height=2, width=50)
label.grid(row=0, column=0, columnspan=2, pady=2)
label_1 = tk.Label(master=app, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 1: {getal_1}")
label_1.grid(row=1, column=0, padx=10)
label_2 = tk.Label(master=app, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 2: {getal_2}")
label_2.grid(row=1, column=1, padx=10)

# Knop gelinkt aan toon_resultaat() maken & plaatsen.
knop = tk.Button(master=app, command=toon_resultaat, text="Bereken resultaat:", width=50)
knop.grid(row=2, column=0, columnspan=2, pady=10)

# Label met resultaat maken & plaatsen.
label_result = tk.Label(master=app, text=f"Het huidige resultaat is: {resultaat}", height=2, width=50)
label_result.grid(row=3, column=0, columnspan=2, pady=2)

app.mainloop()