# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True:
    naam = input("Geef de naam van de gebruiker op: ")
    if naam == "STOP":
        break
    if naam in gasten:
        print(f"Welkom, {gasten[naam]} {naam}. Kom binnen")
        print("--------------------------")
        gasten.pop(naam)
    elif naam not in gasten:
        print(f"De naam {naam} staat niet op de lijst.")
        print("--------------------------")