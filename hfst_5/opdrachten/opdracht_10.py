# Maak een klasse Speler & Spel zoals aangegeven in opdracht 10.
class Speler:
    def __init__(self, naam: str , level: int, score: int) -> None:
        self.naam = naam
        self.level = level
        self.score = score

    def level_up(self):
        self.level += 1
        print(f"{self.naam} is level: {self.level} geworden.")

    def info(self):
        print(f"{self.naam}: level: {self.level}, score: {self.score}")
        
    def verhoog_score(self, punten: int):
        
        if type(punten) != int:
            print(f"'verhoog score' vereist een int, niet: {type(punten)}.")

        else:
            self.score += punten
            print("Score verhoogd")


class Spel:
    def __init__(self, naam: str, spelers: list) -> None:
        self.naam = naam
        self.spelers = spelers

    def speler_toevoegen(self, speler):
        self.spelers.append(speler)
        print(f"{speler} doet mee aan het spel: {self.naam}")

    def scorebord(self):
        print(f"De huidige scores van de spelers in: {self.naam}")
        for speler in self.spelers:
            print(f"{speler.naam} met level: {speler.level}, en score: {speler.score}.")

    def spelen(self):
        