# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for fruit, aantal in fruitmand.items():
    gekocht = int(input(f"Hoeveel {fruit} heeft u gekocht: "))
    fruitmand[fruit] = aantal + gekocht

print("in de fruitmand zitten momenteel:")

for fruit, aantal in fruitmand.items(): 
    print(f"-{aantal} {fruit}")