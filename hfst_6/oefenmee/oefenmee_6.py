def draaiom(woord:str) -> str:
    if len(woord) == 1:
        return woord
    return woord[-1] + draaiom(woord[0:len(woord) -1])

print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI

index = -1
omgedraaidWoord = ""
woord = "Hallo"
while True:
    omgedraaidWoord += woord[index]
    if abs(index) == len(woord):
        break

    index -= 1


print(omgedraaidWoord)