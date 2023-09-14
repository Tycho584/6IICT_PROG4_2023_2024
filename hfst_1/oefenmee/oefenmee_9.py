# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
personen = int(input("Voor hoeveel personen is dit recept?:"))
print("Recept voor worst met wortelen en erwten.")
for ingredient, hoeveelheid in recept.items():
    hoeveelheid = hoeveelheid /4 *personen
    print(f"-{ingredient} :{hoeveelheid} gr.")