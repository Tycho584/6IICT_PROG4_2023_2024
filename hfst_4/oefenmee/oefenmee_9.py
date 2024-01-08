import random

vragen_totaal = 3
vraag_juist, vragen_gesteld = 0, 0
while vragen_totaal != vragen_gesteld:

    try:
        getal_1 = random.randint(0,20)
        getal_2 = random.randint(0,20)
        operator = random.choice("+","-","/","*")

        "VUL VERDER AAN NIVEAU 1"
    except Exception:
        "VUL AAN NIVEAU 2"
    else:
        "VUL AAN NIVEAU 2"
    finally:
        "VUL AAN NIVEAU 3"

print("Quiz afgelopen.")