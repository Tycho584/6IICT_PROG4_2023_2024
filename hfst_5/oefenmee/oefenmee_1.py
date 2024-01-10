class Bier:
    def __init__(self,merk:str ,smaak:str, percentage:float, soort:str, prijsPerLiter:float, verkoopPlaatsen:list) -> None:
        self.merk = merk
        self.smaak = smaak
        self.percentage = percentage
        self.soort = soort
        self.prijsPerLiter = prijsPerLiter
        self.verkoopPlaatsen = verkoopPlaatsen

    def InformatieOpvragen(self):
        print(f"Het bier van het merk {self.merk} met een alcoholpercentage van {self.percentage}% vant onder het soort van {self.soort}.")
        print(f"Het wordt verkocht in de volgende supermarkten: {self.verkoopPlaatsen} tegen deze prijs per liter: €{self.prijsPerLiter}.")

    def prijsPerLiterVeranderen(self,nieuwePrijsPerLiter:float) -> None:
        print(f"De prijs per liter is veranderd van €{self.prijsPerLiter} naar €{nieuwePrijsPerLiter}")
        self.prijsPerLiter = nieuwePrijsPerLiter

    def merkVerpester(self, nieuwMerk:str) -> None:
        print(f"Het merk van het bier is aangpast van: {self.merk} naar: {nieuwMerk}")
        self.merk = nieuwMerk

    def ToevoegenVerkoopPunt(self, verkoopPunt:str) -> None:
        print(f"{verkoopPunt} is als verkooppunt toegevoegd.")
        self.verkoopPlaatsen.append(verkoopPunt)

    def verwijderVerkoopPunt(self,verkoopPunt:str) -> None:
        print(f"{verkoopPunt} is verwijderd als verkooppunt.")
        self.verkoopPlaatsen.pop(verkoopPunt)

class SpeciaalBier(Bier):
    def __init__(self, merk: str, smaak: str, percentage: float, soort: str, prijsPerLiter: float, verkoopPlaatsen: list, catogorie:str) -> None:
        self.catogorie = catogorie
        Bier.__init__(self, merk, smaak, percentage, soort, prijsPerLiter, verkoopPlaatsen)

    def catogorieChecker(self) -> None:
        print(f"De catogorie van dit bier is: {self.catogorie}.")

hertogJanVerkoopPlaatsen = ["Plus", "Albert Heijn", "Aldi"]
afligemVerkoopPlaatsen = ["Plus", "Jan linders", "Albert Heijn", "Aldi", "Lidl", "Dirk", "Gall & Gall"]

hertogJan = Bier("Hertog Jan", "Bitterzoet", 5.1, "pilsner", 15.3, hertogJanVerkoopPlaatsen)

afligem = SpeciaalBier("Afligem", "Bitter", "6.8", "Blond", 5.07, afligemVerkoopPlaatsen, "Gemiddeld")

hertogJan.InformatieOpvragen()
afligem.InformatieOpvragen()
afligem.catogorieChecker()