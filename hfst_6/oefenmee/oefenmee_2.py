# Los de vragen uit oefen mee 2 op.

def optellen(getal):
    if getal == 1:
        print(getal)
        return
    
    optellen(getal-1)
    print(getal)

optellen(3)