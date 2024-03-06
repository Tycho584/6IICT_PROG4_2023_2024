# Maak een klasse Voertuig & Bus zoals aangegeven in opdracht 12.

class Voertuig:
    def __init__(self, merk: str, verbruik: float, zetels: int) -> None:
        self.merk = merk
        self.verbruik = verbruik
        self.zetels = zetels

    def info(self):
        print(f"Het voertuig van merk {self.merk} verbruikt {self.verbruik} l/100km")

class Bus(Voertuig):
    def __init__(self, merk: str, verbruik: float, zetels: int, doel: str) -> None:
        super().__init__(merk, verbruik, zetels)
        self.doel = doel

    def ticket_prijs(self, afstand):
        prijs = 5 / self.zetels * afstand
        return prijs

" Via onderstaande code kan je niveau 1 testen. "
# voertuig_1 = Voertuig("Mercedes", 6.5, 5)
# voertuig_2 = Voertuig("Honda", 4.5, 1)

# voertuig_1.info() # Het voertuig van merk Mercedes verbruikt 6.5 l/100km.
# voertuig_2.info() # Het voertuig van merk Honda verbruikt 4.5 l/100km.


" Via onderstaande code kan je niveau 2 testen. "
# bus_1 = Bus("Hymer", 32.4, 90, "Openbaar Vervoer")
# bus_2 = Bus("Adria", 10.5, 8, "Vakantie busje")

# print( bus_1.ticket_prijs(14)  ) # 0.77
# print( bus_2.ticket_prijs(445) ) # 278.13
