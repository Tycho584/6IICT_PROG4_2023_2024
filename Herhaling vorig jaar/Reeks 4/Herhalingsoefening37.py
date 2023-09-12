""" Maak het spel galgje na.

    Gebruik hiervoor een willekeurig woord uit 
    onderstaande lijst (uitbreiden mag).

    Vraag de gebruiker naar een letter of
    om het woord te raden. Het spel stopt
    als het woord correct is of na 7 vragen.

    Print in het eerste geval "gewonnen!".
    In het tweede geval "verloren!". 

        Tip! stel een lijst op met erin de
             gevonden letters. Vul deze eerst
             volledig met _ . Als de gebruiker een 
             letter geeft die in het woord zit, 
             vervang de overeenkomstige _ door deze 
             letter.

    >>> Gok letter / Raad woord (1/7): a
    Woord:  _  _  _  _
    >>> Gok letter / Raad woord (2/7): e
    Woord:  e  _  e  _
    >>> Gok letter / Raad woord (3/7): t
    Woord:  e  _  e  _
    >>> Gok letter / Raad woord (4/7): v
    Woord:  e  v  e  _
    >>> Gok letter / Raad woord (5/7): even
    gewonnen!
"""
print('opstarten...')
import random
WoordLijst = ['letter', 'galgje', 'woord', 'computer', 'toetsenbord', 'programma', 'camera', 'scherm', 'galg', 'goed', 'stoel', 'spel', 'ananas']
GeheimWoord = WoordLijst[random.randrange(0, len(WoordLijst))]
GeradenLetters = []
levens = 10

def checkWin():
    for i in range(len(GeheimWoord)):
        if not GeheimWoord[i] in GeradenLetters:
            return(False)
    return(True)

def renderWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print('? ', end='')
        print('')
        print('" ' * len(GeheimWoord))
        print("====================================================================")

renderWoord()

while True:
    letter = input('raad een letter of typ het woord  ')
    if len(letter) == 1:
        if letter in GeradenLetters:
            print('Die letter had je al geraden...')
            renderWoord()
        else:
            GeradenLetters += letter
            if letter in GeheimWoord:
                print('Goed. Die letter zit wel in het woord')
                renderWoord()
                if checkWin():
                    print('Je hebt alle letters geraden, en dus gewonnen!')
                    print('Het woord was: ' + GeheimWoord)
                    break
            else:
                print('Fout. Die letter zit niet in het woord')
                print('-1')
                levens -= 1
                renderWoord()
    elif letter == GeheimWoord:
        print('Je hebt het woord geraden, en dus gewonnen!')
        break
    elif letter == len(GeheimWoord):
        print('Fout woord!')
        print('-2')
        levens -= 2
        renderWoord()
    else:
        print("Geef één letter of het woord in, er worden geen levens verwijderd.")
        renderWoord()
    if levens <= 0:
        print('Je hebt verloren! Het woord was ' + GeheimWoord)
        break
    print('Je hebt nog', levens, 'levens over.')
print('Afsluiten...')