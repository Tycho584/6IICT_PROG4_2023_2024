"""
Drukken op de knop van deze app geeft een foutmelding.
Dit omdat de globale variabele getal lokaal wordt aangepast.
Los dit probleem op door gebruik te maken van het sleutelwoord global.

Test de werking door een aantal keer op de knop te klikken.
"""

import tkinter as tk
app = tk.Tk()

getal = 5
def knop_klik():
    getal+=1
    print(getal)

# Klikken op de knop geeft fout. Want getal wijzigen kan niet in de functie.
knop = tk.Button(master=app, text="Klik op mij!", command=knop_klik)
knop.pack() 

app.mainloop()
