class Lid:
    def __init__(self, naam):
        self.voornaam, self.achternaam = naam.split(" ")

    def voorstellen(self):
        return f"Hey, mijn naam is {self.voornaam}."
    
    def beschrijving(self):
        return None


class Student(Lid):
    def __init__(self, naam, reden):
        super().__init__(naam)
        self.reden = reden
        self.interesses = []

    def beschrijving(self):
        print(self.reden)

    def interesse_toevoegen(self, interesse):
        if interesse in self.interesses:
            print(f"{interesse} is reeds een interesse van {self.voornaam}.")
            return
        self.interesses.append(interesse)

    def interesse_verwijderen(self, interesse):
        if interesse not in self.interesses:
            print(f"{interesse} is geen een interesse van {self.voornaam}.")
            return  
        self.interesses.remove(interesse)


class Instructeur(Lid):
    def __init__(self, naam, bio):
        super().__init__(naam)
        self.bio = bio
        self.skills = []

    def beschrijving(self):
        print(self.bio)

    def skill_toevoegen(self, skill):
        if skill in self.skills:
            print(f"{skill} is reeds een skill van {self.voornaam}.")
            return
        self.skills.append(skill)


class Workshop:
    def __init__(self, datum, onderwerp):
        self.datum = datum
        self.onderwerp = onderwerp
        self.instructeurs = []
        self.studenten = []

    def deelnemer_toevoegen(self, lid):       
        if isinstance(lid, Student):
            if self.onderwerp not in lid.interesses:
                print(f"{lid.voornaam} heeft geen interesse in deze workshop.")
                return
            self.studenten.append(lid)

        elif isinstance(lid, Instructeur):
            if self.onderwerp not in lid.skills:
                print(f"{lid.voornaam} heeft geen skill om deze workshop te geven.")
                return
            self.instructeurs.append(lid)

    def update(self):
        for student in self.studenten:
            if self.onderwerp not in student.interesses: 
                self.studenten.remove(student)
        for instructeur in self.instructeurs:
            if self.onderwerp not in instructeur.skills: 
                self.instructeur.remove(student)       
        
    def info(self):
        tekst = f"Workshop - {self.datum} - {self.onderwerp}\n\n"
        tekst += f"Totaal aantal deelnemers: {len(self.studenten) + len(self.instructeurs)}\n\n"

        tekst += "Studenten:\n"
        for index, student in enumerate(self.studenten):
            tekst += f"{index+1}. {student.voornaam} {student.achternaam} - {','.join(student.interesses)}\n"
        tekst += "\nInstructeurs:\n"
        for index, instructeur in enumerate(self.instructeurs):
            tekst += f"{index+1}. {instructeur.voornaam} {instructeur.achternaam} - {','.join(instructeur.skills)}\n"

        print(tekst)

