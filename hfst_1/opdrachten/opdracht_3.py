# Start met onderstaande dictionary.
database = { # Sleutel = naam, waarde = wachtwoord
    "Jan": "FkeHsne569*",
    "Piet": "KsnOmd727^",
    "Joris": "DneSje439&",
    "Korneel": "MdsSnz863*"
}
naam = input("Wat is uw naam?: ")
if naam in database:
    ww = input("Wat is uw wachtwoord: ")
    teller = 0
    for naam,wachtwoord in database.items():
        if ww == wachtwoord:
            print("Welkom!")
            break
        else:
            teller += 1

    if teller == 4:
        print("Onjuist wachtwoord")
        
else:
    print("Gebruiker bestaat niet")