# Start de oefen mee met onderstaande dictionary.
persoonsinfo = { # info over een persoon
    "naam": "Jan",
    "leeftijd": 32,
    "massa": 79
}
print(f"{persoonsinfo['naam']} is {persoonsinfo['leeftijd']} jaar oud & weegt {persoonsinfo['massa']} kg.")

print( len( persoonsinfo ) )

# oogkleur = persoonsinfo["oogkleur"]
# print(f"Deze persoon heeft {oogkleur} ogen.")

naam = "Jan"
print(persoonsinfo[naam])
