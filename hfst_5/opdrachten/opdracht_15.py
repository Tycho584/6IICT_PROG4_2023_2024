class Lid:
    def __init__(self, voorNaam: str, achterNaam: str) -> None:
        self.voorNaam = voorNaam
        self.achterNaam = achterNaam

    def voorstellen(self):
        print(f"Hallo, mijn naam is: {self.voorNaam}.")

    def beschrijving(self):
        return None

class Student(Lid):
    def __init__(self, voorNaam: str, achterNaam: str, reden: str, interesses: list) -> None:
        super().__init__(voorNaam, achterNaam)
        self.reden = reden
        self.interesses = interesses

    def interesseToevoegen(self, nieuweInteresses: list):
        for interesse in nieuweInteresses:
            if interesse not in self.interesses:
                self.interesses.append(interesse)

            elif interesse in self.interesses:
                print("Interesse is reds in de lijst met interesses.")

    def interesseVerwijderen(self, interesse):
        if interesse in self.interesses:
            self.interesses.pop(interesse)

        elif interesse not in self.interesses:
            print("Deze interesse zit niet in de lijst met interesses.")

    def beschrijving(self):
        print(f"De reden dat ik hier ben is: {self.reden}.")

class Instructeur(Lid):
    def __init__(self, voorNaam: str, achterNaam: str, bio: str, skills: list) -> None:
        super().__init__(voorNaam, achterNaam)
        self.bio = bio
        self.skills = skills

    def skillToevoegen(self, nieuweSkills: list):
        for skill in nieuweSkills:
            if skill not in self.skills:
                self.skills.append(skill)

            elif skill in self.skills:
                print()

    def beschrijving(self):
        print(f"Mijn bio is: {self.bio}.")

class Workshop:
    def __init__(self, datum: str, onderwerp: str, instructeurs: list, studenten: list) -> None:
        self.datum = datum
        self.onderwerp = onderwerp
        self.instructeurs = instructeurs
        self.studenten = studenten

    def delnemersToevoegen(self, deelnemer):
        if type(deelnemer) == Student:
            if self.onderwerp in deelnemer.interesses:
                self.studenten.append(deelnemer)
            else:
                print(f"{deelnemer.voorNaam} is niet geïnteresserd in deze workshop.")

        elif type(deelnemer) == Instructeur:
            if self.onderwerp in deelnemer.skills:
                self.instructeurs.append(deelnemer)
            else:
                print(f"{deelnemer.voorNaam} heft niet de juiste skillset voor deze workshop.")

    def update(self):
        for student in self.studenten:
            if self.onderwerp not in student.interesses:
                self.studenten.pop(student)

        for instructeur in self.instructeurs:
            if self.onderwerp not in instructeur.bio:
                self.instructeurs.pop(instructeur)

    def info(self):
        print(f"Workshop - {self.datum} - {self.onderwerp}")
        print(f"\n Totaal aantal delnemers: {len(self.instructeurs) + len(self.studenten)}")
        print("\nStudenten")

        for index, student in enumerate(self.studenten):
            print(f"{index + 1}. {student.voorNaam} {student.achterNaam} - {student.interesses}")

        print("\nInstruceurs")
    
        for index, Instructeur in enumerate(self.instructeurs):
            print(f"{index + 1}. {Instructeur.voorNaam} {Instructeur.achterNaam} - {Instructeur.skills}")