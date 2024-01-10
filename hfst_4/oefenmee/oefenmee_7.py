fruit_lijst = ["Appel", "Banaan", "Kers"]
try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
    
except IndexError:
    print( "Er is een foute indexering ingegeven." ) 

except ValueError:
    print("er is een ongeldig getal ingegeven (of een string).")

print("Programma klaar") 