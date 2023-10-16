""" Dit is een extra oefen mee!
In onderstaande app moet de functie bereken_erlangs nog gemaakt worden.
Vul deze aan op basis van de instructies in de functie.

Voorbeelden en een uitgebreidere uitleg van de werking zijn te vinden bij oefen mee 17.
"""

# Importeer tkinter module. Geef naam tk.
# Importeer random module
import tkinter as tk, random

# Maak een lege GUI aan.
app = tk.Tk()

random_getal = -1
def genereer():
    # Breng de variabele random_getal in de functie.
    global random_getal
    # Lees de waarde van entry_1 uit.
    tekst = entry_1.get()

    # Enkel als tekst een getal is, mag random.randint() uitgevoerd worden.
    if not tekst.isnumeric():
        resultaat = "Entry slecht ingevuld!"
    else:
        random_getal = random.randint(0, int(tekst))
        resultaat = "Getal berekend!"

    # Wijzig de inhoud van Label label_genereer
    label_genereer.config(text=resultaat)

def bereken_erlangs():
    """ TODO:

    Deze functie is gelinkt aan de Button knop_2.
    
    - Het drukken op de knop berekent hoeveel de gok van de gebruiker,
      langs het willekeurige getal zat.
    - Vervolgens wordt het Label label_bereken aangepast om deze berekening te tonen.
    - Als de input van de gebruiker niet geldig is, moet label_bereken in plaats hiervan
      de melding 'Entry slecht ingevuld!' tonen.
    
    """

# Zet labels met uitleg klaar.
label = tk.Label(padx=40, pady=5, master=app, text="Geef een getal in: ")
label.grid(row=0, column=0)
label = tk.Label(padx=40, pady=5, master=app, text="Gok het gegenereerde getal: ")
label.grid(row=0,column=1)

# Zet invulvelden klaar.
entry_1 = tk.Entry() 
entry_1.grid(row=1, column=0)
entry_2 = tk.Entry()
entry_2.grid(row=1, column=1) 

# Zet knoppen klaar.
knop_1 = tk.Button(pady=10, master=app, text="Genereer getal", command=genereer)
knop_1.grid(row=2, column=0)
knop_2 = tk.Button(pady=10, master=app, text="Gok het getal", command=bereken_erlangs)
knop_2.grid(row=2, column=1)

# Zet labels met resultaten van knoppen klaar.
label_genereer = tk.Label(padx=40, pady=5, master=app, text="")
label_genereer.grid(row=3,column=0)
label_bereken = tk.Label(padx=40, pady=5, master=app, text="")
label_bereken.grid(row=3,column=1)

# Maak de GUI zichtbaar op de computer.
app.mainloop()