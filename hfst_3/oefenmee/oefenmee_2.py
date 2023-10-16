"""
VOER DE CODE NOG NIET UIT!
"""
import tkinter as tk
app = tk.Tk()

label_1 = tk.Label(master=app, text="Label 1")
label_1.grid(row=1, column=0) # Rij 1, kolom 0

label_3 = tk.Label(master=app, text= "Label 3")
label_3.grid(row=3, column=0) # Rij 3, kolom 0

label_5 = tk.Label(master=app, text= "Label 5")
label_5.grid(row=5, column=0) # Rij 5, kolom 0

app.mainloop()
