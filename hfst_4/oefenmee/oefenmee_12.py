def deel(teller, noemer):
    return teller/noemer

" Voorbeelden om de werking van functie deel te testen. "
# print( deel(8, 2) )      # 4.0

# print( deel(9, 0) )      # ZeroDivisionError: Snul.
# print( deel(True, 4) )   # TypeError: True is <class 'bool'>, moet int/float zijn.
# print( deel(8, "a")  )   # TypeError: a is <class 'str'>, moet int/float zijn.
# print( deel(True, "a") ) # TypeError: True is <class 'bool'>, moet int/float zijn.