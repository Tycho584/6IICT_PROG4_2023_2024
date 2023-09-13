# Vul onderstaande dictionary aan met behulp van input.
relaties = {}

while True:
    sleutel = input("Geef uw relatie tot de persoon in: ")
    waarde = input("geef de naam van de persoon in: ")

    if sleutel == "STOP" or waarde == "STOP":
        break
    else:
        if sleutel in relaties:
            print("Kan relatie niet toevoegen, deze bestaat al")
            print("----------------")
        else: 
            relaties[sleutel] = waarde
            print("----------------")


print(relaties)