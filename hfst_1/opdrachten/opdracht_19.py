# Dictionary met vluchten en passagiersgegevens
vlucht_reservering_systeem = {
    'vluchten': {
        'VL001': {
            'van': 'New York',
            'naar': 'Los Angeles',
            'vertrektijd': '2023-09-01 10:00',
        },
        'VL002': {
            'van': 'Chicago',
            'naar': 'Miami',
            'vertrektijd': '2023-09-02 12:00',
        },
        # Meer vluchtvermeldingen...
    },
    'passagiers': {
        'P001': {
            'naam': 'Alice Smith',
            'geboekte_vluchten': ['VL001'],
        },
        'P002': {
            'naam': 'Bob Johnson',
            'geboekte_vluchten': ['VL002'],
        },
        # Meer passagiersvermeldingen...
    }
}

# Functie om vluchten te boeken (Niveau 1)
def boek_vlucht():
    naam = input("Geef uw naam op: ")
    
    # Controleer of de passagier al bestaat, anders maak een nieuwe passagier aan
    if naam not in [passagier['naam'] for passagier in vlucht_reservering_systeem['passagiers'].values()]:
        nieuwe_passagier_id = f'P{len(vlucht_reservering_systeem["passagiers"]) + 1:03d}'
        vlucht_reservering_systeem['passagiers'][nieuwe_passagier_id] = {'naam': naam, 'geboekte_vluchten': []}
    
    # Toon beschikbare vluchten
    print("Beschikbare vluchten:")
    for vlucht_id, vlucht_info in vlucht_reservering_systeem['vluchten'].items():
        print(f"{vlucht_id}: Van {vlucht_info['van']} naar {vlucht_info['naar']}")
    
    vlucht_id = input("Geef de Vlucht-ID op: ")
    
    if vlucht_id not in vlucht_reservering_systeem['vluchten']:
        print("Deze Vlucht-ID bestaat niet. Probeer opnieuw.")
        return
    
    passagier_id = [passagier for passagier, info in vlucht_reservering_systeem['passagiers'].items() if info['naam'] == naam][0]
    
    if vlucht_id in vlucht_reservering_systeem['passagiers'][passagier_id]['geboekte_vluchten']:
        print("U heeft deze vlucht al geboekt.")
        print("-------------------------------------------------------------------------")
    else:
        vlucht_reservering_systeem['passagiers'][passagier_id]['geboekte_vluchten'].append(vlucht_id)
        print(f"Vlucht {vlucht_id} is geboekt voor {naam}.")
        print("-------------------------------------------------------------------------")
    
    # Toon overzicht van geboekte vluchten
    print(f"Uw geboekte vluchten:")
    for geboekte_vlucht in vlucht_reservering_systeem['passagiers'][passagier_id]['geboekte_vluchten']:
        vlucht_info = vlucht_reservering_systeem['vluchten'][geboekte_vlucht]
        print(f"{geboekte_vlucht}: Van {vlucht_info['van']} naar {vlucht_info['naar']}")
        print("-------------------------------------------------------------------------")

# Functie om lijst van passagiers op een vlucht te tonen (Niveau 2)
def toon_passagiers_op_vlucht():
    # Toon beschikbare vluchten
    print("Beschikbare vluchten:")
    for vlucht_id, vlucht_info in vlucht_reservering_systeem['vluchten'].items():
        print(f"{vlucht_id}: Van {vlucht_info['van']} naar {vlucht_info['naar']}")
        print("-------------------------------------------------------------------------")
    
    vlucht_id = input("Geef de Vlucht-ID op: ")
    print("-------------------------------------------------------------------------")
    
    if vlucht_id not in vlucht_reservering_systeem['vluchten']:
        print("Deze Vlucht-ID bestaat niet. Probeer opnieuw.")
        print("-------------------------------------------------------------------------")
        return
    
    print(f"Passagiers op vlucht {vlucht_id}:")
    print("-------------------------------------------------------------------------")
    for passagier_id, passagier_info in vlucht_reservering_systeem['passagiers'].items():
        if vlucht_id in passagier_info['geboekte_vluchten']:
            print(passagier_info['naam'])

# Hoofdprogramma
while True:
    print("Dag beste gebruiker. Waarmee kan ik helpen?")
    print("1) Boeken van een vlucht.                ")
    print("2) Lijst van passagiers op vlucht tonen. ")
    print("3) Stoppen.                              ")
    print("-------------------------------------------------------------------------")
    
    optie = input("Welke optie selecteren: ")
    print("-------------------------------------------------------------------------")
    
    if optie == '1':
        boek_vlucht()
    elif optie == '2':
        toon_passagiers_op_vlucht()
    elif optie == '3':
        print("Bedankt voor het gebruik van de app. Tot ziens!")
        break
    else:
        print("Ongeldige optie. Probeer opnieuw.")
        print("-------------------------------------------------------------------------")
