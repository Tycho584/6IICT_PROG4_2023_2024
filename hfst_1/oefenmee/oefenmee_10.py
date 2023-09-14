# Vul eerst aan. Daarna pas uitvoeren!
dictionary = {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}

""" Geef aan wat volgende code print"""
" Vul aan: "
print(dictionary)
#"a": 0, "b": 1, "c": 1, "d": 2, "e": 3

" Vul aan: "
for x in dictionary:
    print(x)
    #0,1,1,2,3

" Vul aan: "
print( list(dictionary.keys()))
#a,b,c,d,e

" Vul aan: "
print( dictionary.get("e", 4))
#e

" Vul aan: "
print( list(dictionary.values()))
#0,1,1,2,3

" Vul aan: "
print( dictionary.get("q", 4))
#4

" Vul aan: "
for x, y in dictionary.items():
    print(y, x)
#a,0,b,1,c,1,d,2,e,3

" Vul aan: "
for x in dictionary.values():
    print(x)
#0,1,1,2,3

" Vul aan: "
print( dictionary.pop("c"))
#1

"Vul aan: "
print( list(dictionary.items()) )
# een lijst van de dictionary sleutels en waardes
