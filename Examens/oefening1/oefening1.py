""" Niveau 1 
Je kan onderstaande inputwoorden gebruiken om de code te testen.
Naast ieder inputwoord staat het best aansluitende woord uit het woordenboek en de behaalde score.

inputwoord = "testen" # aansluitend = "testen"  , score = 0    !! Exacte match !!
inputwoord = "fijne"  # aansluitend = "fijn"    , score = 0.2
inputwoord = "yxqzhh" # aansluitend = "Kyrmisch", score = 0.75 !! Geen goede match !!

"""



""" Niveau 2
Je kan onderstaande zin gebruiken om de code te testen.
inputzin = "Een #fijne zomervakantie gewenst... allemaal! :)"

Na verwerken moet deze zin er als volgt uitzien.
"een fijne zomervakantie gewenst allemaal"
!! opgelet: code moet alle speciale tekens verwijderen, ongeacht hun positie in de zin !!

Voer tenslotte de code uit niveau 1 uit op ieder woord van deze inputzin.

een:           een (exacte match)
fijne:         fijn
zomervakantie: zomervakantie (exacte match)
gewenst:       gewest
allemaal:      allemaal (exacte match)

"""

import Levenshtein, json

specialeTkensLijst = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',"\",':',';','"',''','<',',','>','.','?','/'}


laagsteScore = 2
referentieWoord = "/"

inputwoord = input("Inputwoord:: ")

with open("Examens\oefening1\oefening1_woordenboek.json", "r") as file: 
    fileContent = json.load(file)

inputwoord = inputwoord.lower()

for woord in fileContent:
    levenshteinAfstandTotSpecifiekWoord = Levenshtein.distance(inputwoord, woord)
    levenshteinAfstandTotSpecifiekWoord /= max(len(woord), len(inputwoord))

    if levenshteinAfstandTotSpecifiekWoord < laagsteScore:
        laagsteScore = levenshteinAfstandTotSpecifiekWoord
        referentieWoord = woord
        referentieWoord = referentieWoord.lower()

if laagsteScore == 0:
    print(f"Het woord dat hier het meest op lijkt is: {referentieWoord}, en de Levenshteinscore hiervan is: {laagsteScore} (Exacte match).")

elif laagsteScore <= 0.7:
        print(f"Het woord dat hier het meest op lijkt is: {referentieWoord}, en de Levenshteinscore hiervan is: {laagsteScore}.")
elif laagsteScore >= 0.7:
    print(f"Het woord dat hier het meest op lijkt is: {referentieWoord}, en de Levenshteinscore hiervan is: {laagsteScore} (Basisvorm van dit woord staat waarschijnlijk niet in het woordenboek).")
