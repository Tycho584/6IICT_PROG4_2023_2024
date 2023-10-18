"""
Maak de app na volgens de foto bij oefen mee 3.
Je hebt maar 3 labels nodig om deze app te maken.
"""
import tkinter as tk

app = tk.Tk()

label_1 = tk.Label(master=app, text="Hallo")
label_1.grid(row=0, column=0)

label_2 = tk.Label(master=app, text="klas")
label_2.grid(row=0, column=1)

label_3 = tk.Label(master=app, text="6IICT!")
label_3.grid(row=1, column=1)

app.mainloop()