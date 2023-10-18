"""
Volg de instructies van oefen mee 10.
Je zal een app maken waarmee je de eerste/laatste letter uit een entry kan verwijderen.
De app bestaat uit 1 entry & 2 buttons.

"""

import tkinter as tk

def eerste():
    veld.delete(0,1)

def laatste():
    woord = veld.get()
    woord = woord [:-1]
    veld.delete(0,tk.END)
    veld.insert(0,woord)

app = tk.Tk()
app.title("Letter verwijderaar")

veld = tk.Entry(master=app)
veld.grid(row=0, column=0, columnspan=2)

knop_eerste = tk.Button(master=app, text="Verwijder Eerste!", command=eerste)
knop_eerste.grid(row=1, column=0)

knop_laatste = tk.Button(master=app, text="Verwijder Laatste!", command=laatste)
knop_laatste.grid(row=1, column=1)

app.mainloop()