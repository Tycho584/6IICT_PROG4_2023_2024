"""
Volg de instructies van oefen mee 8.
Je zal een simpel rekenmachine maken met behulp van 2 Entries, 1 label & 1 button.
    
    Tip! De methode .get() van entries geeft altijd een string.
         Je kan hier natuurlijk niet mee rekenen.
"""
import tkinter as tk

app = tk.Tk()

def bereken():
    getal_1 = veld_1.get()
    getal_2 = veld_2.get()

    if not getal_1.isnumeric() or not getal_2.isnumeric():
        label.config(text="GEEF GETALLEN IN !!!!!!")
    else:
        getal_1 = int(getal_1)
        getal_2 = int(getal_2)
        label.config(text=f"De som van bovenstaande getallen is: {getal_1 + getal_2}")

veld_1 = tk.Entry(master=app)
veld_1.grid(row=0, column=0)

veld_2 = tk.Entry(master=app)
veld_2.grid(row=0,column=1)

label = tk.Label(master=app, text="")
label.grid(row=1,column=0, columnspan=2)

knop = tk.Button(master=app, text="Uitberekenen", fg="yellow", bg="red", command=bereken)
knop.grid(row=2, column=0, columnspan=2)

app.mainloop()