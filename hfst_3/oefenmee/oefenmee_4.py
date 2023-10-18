"""
Maak de app na volgens de foto bij oefen mee 3.
Je zal de parameters columnspan & rowspan van .grid() moeten gebruiken.
"""
import tkinter as tk

app = tk.Tk()

label_1 = tk.Label(master=app, text="(0;0)")
label_1.grid(row=0, column=0)

label_2 = tk.Label(master=app, text="(0;1)")
label_2.grid(row=0, column=1)

label_3 = tk.Label(master=app, text="(0;2)")
label_3.grid(row=0, column=3)

label_4 = tk.Label(master=app, text="(1;0)")
label_4.grid(row=1, column=0)

label_5 = tk.Label(master=app, text="(1;1)-columnspan = 2")
label_5.grid(row=1, column=1, columnspan=2)

label_6 = tk.Label(master=app, text="(2;0)-rowspan = 2")
label_6.grid(row=2, column=0,rowspan=2)

label_7 = tk.Label(master=app, text="(2;1)")
label_7.grid(row=2, column=1)

label_8 = tk.Label(master=app, text="(2;2)")
label_8.grid(row=2, column=2)

label_9 = tk.Label(master=app, text="(3;1)")
label_9.grid(row=3, column=1)

label_10 = tk.Label(master=app, text="(3;2)")
label_10.grid(row=3, column=2)

app.mainloop()