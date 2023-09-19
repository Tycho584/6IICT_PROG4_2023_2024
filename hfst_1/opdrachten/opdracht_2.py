# Maak onderstaande functie af.
persoonsinfo = {}
def maak_persoonsinfo(naam, leeftijd, massa, lengte):
    persoonsinfo["naam"] = naam
    persoonsinfo["leeftijd"] = leeftijd
    persoonsinfo["massa"] = massa
    persoonsinfo["lengte"] = lengte
    return persoonsinfo

info = maak_persoonsinfo("Jan", 32, 79, 167)
print(info) # {'naam': 'Jan', 'leeftijd': 32, 'massa': 79, 'lengte': 167}