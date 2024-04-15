# Bepaal de faculteit van een getal met behulp van een while-loop.

def facul(getal:int) -> None:

    faculteit = 1
    uitkomst = 0
    while True:
        if getal == 1:
            break

        getal = getal * faculteit    

print( facul(1) ) # 1
print( facul(2) ) # 2
print( facul(3) ) # 6
print( facul(4) ) # 24
print( facul(5) ) # 120