# Los de vragen uit oefen mee 3 op.


def facul(n):
    if n == 1:
        return 1
    
    vorige_faculteit = facul( n-1 )
    return n * vorige_faculteit

n = 3
print( facul(n) ) # Faculteit van 3: 6