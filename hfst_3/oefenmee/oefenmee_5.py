"""
Analyseer onderstaande code. Let vooral op 'command=maak_label'.
Beantwoord vervolgens de vragen bij oefen mee 5.
"""

import tkinter as tk
app = tk.Tk()

# Functie maakt & plaatst een label.
def maak_label():
    label = tk.Label(master=app, text="Goed gedaan!")
    label.pack()

# 1) Knop aanmaken.
knop = tk.Button(master=app, text="Klik op mij!", command=maak_label)
# 2) Knop plaatsen.
knop.pack()

app.mainloop()
