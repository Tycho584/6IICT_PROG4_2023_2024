""" OEFENING 3: (  / 5)

!!! OPGELET: voor deze oefening mag je het internet NIET gebruiken. !!!

Gebruik recursie om te controleren hoe vaak een bepaalde letter voorkomt in een string.
je mag tijdens deze oefening geen gebruik maken van count, find, of soortgelijke functies.

TIP:
    hallo = h + allo
                allo = a + llo
                ...
"""

def aantal_letter(gewensteLetter, woord):
    aantal_correcte_letters = 0
    if len(woord) == 0:
        return aantal_correcte_letters
    
    letter = woord[0]
    if letter == gewensteLetter:
        aantal_correcte_letters += 1

    aantal_correcte_letters += aantal_letter(gewensteLetter, woord[1:])
    return aantal_correcte_letters


print( aantal_letter("a", "hallo") )        # 1
print( aantal_letter("r", "programmeren") ) # 3
print( aantal_letter("b", "") )             # 0