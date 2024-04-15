def luhn(cardNumber: int) -> int:
    sum = 0

    cardNumberList = list(str(cardNumber))
    
    for index, number in enumerate(cardNumberList):

        if (index + 1) % 2 == 1:
            number *= 2

            if int(number) > 9:
                number = int(number) - 9
        
        sum += int(number)
    
    return sum
    
        


print( luhn(4687612962034330) ) # 70 --> geldig
print( luhn(6728003096702784) ) # 70 --> geldig
print( luhn(2727903413621029) ) # 66 --> ongeldig
print( luhn(9727009535679498) ) # 92 --> ongeldig