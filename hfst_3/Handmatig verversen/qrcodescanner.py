import qrcode
import tkinter as tk
from PIL import ImageTk, Image

app = tk.Tk()

app.title("QR Code scanner")

text_veld = tk.Entry(master = app)
text_veld.grid(row=0, column=50)

label = tk.Label(app)
label.grid(row=2, column=0, columnspan=100)

def qr_maken():
    img = qrcode.make(text_veld.get())
    img.save("some_file.png")

    img = ImageTk.PhotoImage(Image.open("some_file.png"))

    label.config(image=img)
    label.image = img


while True:
    qr_maken()
    app.update()