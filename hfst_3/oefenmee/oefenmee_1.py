""" 
Maak een app aan die 3 labels bevat.
De inhoud van de 3 labels is:
    - Label 1: hallo
    - Label 2: klas
    - Label 3: 6iict
"""
import tkinter as tk

app = tk.Tk()

label_1 = tk.Label(master=app, text="hallo")
label_1.grid(row=0, column=1)

label_2 = tk.Label(master=app, text="klas")
label_2.grid(row=0, column=2)

label_3 = tk.Label(master=app, text="6IICT")
label_3.grid(row=0, column=3)

app.mainloop()