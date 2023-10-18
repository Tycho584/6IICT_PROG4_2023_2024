"""
Volg de instructies van oefen mee 9.
Je zal een app maken om letters toe te voegen aan een entry op een specifieke positie?
De app bestaat uit 3 entries & 1 button.

"""

import tkinter as tk

app = tk.Tk()

def toevoegen():
    index = veld_index.get()
    letter = veld_letter.get()

    veld_uitkomst.insert(index, letter)

veld_index = tk.Entry(master=app)
veld_index.grid(row=0, column=0)

veld_letter = tk.Entry(master=app)
veld_letter.grid(row=0, column=1)

veld_uitkomst = tk.Entry(master=app)
veld_uitkomst.grid(row=2, column=0, columnspan=2)

knop = tk.Button(master=app, text="Bereken", command=toevoegen)
knop.grid(row=1, column=0, columnspan=2)

app.mainloop()