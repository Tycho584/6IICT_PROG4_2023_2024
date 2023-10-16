"""
In onderstaande app moet de functie toevoegen nog gemaakt worden.
Vul deze aan op basis van de instructies in de functie.

Voorbeelden en een uitgebreidere uitleg van de werking zijn te vinden bij oefen mee 16.
"""

import tkinter as tk

app = tk.Tk()

zin = ""
def toevoegen():
    """TODO: 
    Deze functie is gelinkt aan de Button knop.

    - Het drukken op de knop moet de huidige inhoud van Entry veld toevoegen
      aan de globale variabele zin.
    - Update vervolgens het Label label_zin met de nieuwe waarde van deze variabele.
    - Tenslotte moet de Entry veld leeggemaakt worden.
    """
    
veld = tk.Entry(master=app, font=("Helvetica",14), border=10, borderwidth=5)
veld.grid(row=0, column=0)

knop = tk.Button(master=app, command=toevoegen, text="Voeg toe aan de zin:", width=50)
knop.grid(row=1, column=0, pady=10, padx= 10)

label_zin = tk.Label(master=app, text=f"", height=2) # Het label start leeg.
label_zin.grid(row=2, column=0, pady=10)

app.mainloop()