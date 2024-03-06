# Los de vragen uit oefen mee 1 op.

def aftellen(getal):
    if getal < 1:
        return
    print(getal)
    aftellen(getal-1)

getal = 5
aftellen(getal)
