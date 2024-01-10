from pytube import YouTube
import tkinter as tk


def check():
    url = urlEntry.get()

    yt = YouTube(url)
    print(f"Title: {yt.title}\nAuthor: {yt.author}\nLength: {yt.length} seconden\nAge Ristricted: {yt.age_restricted} ")


root = tk.Tk()

root.geometry("650x250")

resoluties = [144, 240, 360, 480, 720, 1080, 1440, 2160, 4320]
resolutieVar = tk.StringVar(root)
resolutieVar.set(resoluties[0])

resolutieMenu = tk.OptionMenu(root, resolutieVar, *resoluties)

youtubeURLLabel = tk.Label(root, text="Geef een Youtube URL in:", fg="red")
resolutieKiezerLabel = tk.Label(root, text="Welke resolutie downloaden", fg = "gray")

resolutieMenu.grid(row= 3, column= 0,columnspan= 3)

urlEntry = tk.Entry(root, width=100)

checkButton = tk.Button(root, text="Check", command=check)
downloadButton = tk.Button(root,text="Download")

youtubeURLLabel.grid(row=0, column=0, columnspan=3)
resolutieKiezerLabel.grid(row=2, column=0, columnspan=3)
urlEntry.grid(row=1,column=0,columnspan=3)

checkButton.grid(row= 4, column= 0)
downloadButton.grid(row= 4, column=2)


root.mainloop()



# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# yt = YouTube(url)
# print(f"Titel: {yt.title}\nMaker: {yt.author}\nLengte: {yt.length} seconden")
# stream = yt.streams.filter(file_extension="mp4", progressive=True, resolution="720p").first()
# stream.download()