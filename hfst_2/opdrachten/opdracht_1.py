import requests, json, time

stoppen = True


while stoppen:

    goede_catogorie = True
    juist_aantal = True

    print("Van welke catogorie zou u een grpje willen hebben?:")
    print("1) Maakt mij niet zoveel uit, kies maar.")
    print("2) Een in mijn vakgebied, een lekker computer grapje.")
    print("3) Een mopje uit een catogorie met gemengde mopjes. ")
    print("4) Een duister mopje die mischien niet veilig is voor school.")
    print("5) Een woordspelingsgrapje, ik lag me deuk.")
    print("6) Een spooky grapje.")
    print("7) Een grap die je alleen kan maken in de December maand: Kerst.")
    print("-"*60)

    catogorie = int(input("De verkozen catogotie: "))
    print("-"*60)

    if catogorie == 1:
        url_einde = "Any"
    elif catogorie == 2:
        url_einde = "Programming"
    elif catogorie == 3:
        url_einde = "Miscellaneous"
    elif catogorie == 4:
        url_einde = "Dark"
    elif catogorie == 5:
        url_einde = "Pun"
    elif catogorie == 6:
        url_einde = "Spooky"
    elif catogorie == 7:
        url_einde = "Christmas"
    else:
        print("Deze catogorie bestaat niet, geef een bestaande catogorie op.")
        print("-"*60)
        goede_catogorie = False
        time.sleep(5)

    if goede_catogorie:
        aantal = int(input("Hoeveel grapjes zou je willen hebben? [1-5]: "))
        print("-"*60)

        if aantal < 1 or aantal > 5:
            juist_aantal = False

        if juist_aantal:
            if aantal == 1:

                url = f"https://v2.jokeapi.dev/joke/{url_einde}"
                response = requests.get(url)
                response_json = response.json()

                with open("hfst_2/opdrachten/jokeAPI.json", "w") as file:
                    json.dump(response_json, file)
                    if "joke" in response_json:
                        print(response_json["joke"])
                    else:
                        print(response_json["setup"])
                        print(response_json["delivery"])
            else:
                url = f"https://v2.jokeapi.dev/joke/{url_einde}?amount={aantal}"
                response = requests.get(url)
                response_json = response.json()

                for grap in range(aantal):
                    lolletje = response_json["jokes"][grap]
                    with open("hfst_2/opdrachten/jokeAPI.json", "w") as file:
                        json.dump(response_json, file)
                        if "joke" in lolletje or "single" in lolletje:
                            print(response_json["jokes"][grap]["joke"])
                        else:
                            print(response_json["jokes"][grap]["setup"])
                            print(response_json["jokes"][grap]["delivery"])
                            print("="*60)
                
            print("-"*60)
            time.sleep(2)

            vraag = input("Wil je nog een mopje horen?: [y/n]: ")
            if vraag == "y":
                stoppen = True
            elif vraag == "n":
                print("-"*60)
                print("-"*60)
                print("Ok, Het programma wordt stop gezet.")
                print("-"*60)
                print("-"*60)
                stoppen = False