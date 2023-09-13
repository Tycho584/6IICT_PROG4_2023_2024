# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
sleutel = input("Welk soort fruit zoek je?: ")
if sleutel in fruitmand:
    waarde = fruitmand[sleutel]
    print(f"Aantal {sleutel} in de mand: {waarde}")
elif sleutel not in fruitmand:
    print(f"kon {sleutel} niet vinden in de fruitmand")