# Niveau 1: bepaal sommatie van een getal recursief.
def sommatie(getal):
    if getal == 0:
        return getal
    uitkomst = getal + sommatie(getal-1)
    return uitkomst



# Niveau 2: bepaal sommatie van een getal met while-loop.
getal = 10
uitkomst = 0

while True:
    uitkomst = uitkomst + getal
    getal -= 1
    print(uitkomst)

    if getal == 0:
        break


print( sommatie(1) )   # 1
print( sommatie(2) )   # 3
print( sommatie(3) )   # 6
print( sommatie(4) )   # 10
print( sommatie(5) )   # 15
print( sommatie(100) ) # 5050
