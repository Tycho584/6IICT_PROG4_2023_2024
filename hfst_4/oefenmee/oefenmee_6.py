fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )

try: 
    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)

except ValueError:
    print("Geef een geldig getal op!!! (alleen een integer)")

except IndexError:
    print("Geef een getal van een index binnen de lijst op!!!")
    