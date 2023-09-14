# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 8,
    "Werk":  8,
    "Ontspanning": 8
}
teller = 0
print("Planning van morgen")
for onderdeel, tijd in planner.items():
    print(f"{onderdeel} : {tijd} u.")
    if teller == 0:
        tijd = 16
        teller+= 1
    elif teller == 1:
        tijd = 8
        teller+=1
    elif teller == 2:
        tijd = 0
        teller+=1
    print(f"u heeft nog {tijd} over")