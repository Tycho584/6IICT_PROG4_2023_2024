# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
stad = input("Geef uw stad in: ")
if stad in steden_temp:
    print(f"Het is {steden_temp[stad]}C")
else:
    print(f"{stad} bestaat niet. Het is in België 22°C.")