""" OEFENING 2: (  / 10)
Ontwikkel onderstaande klassen. Ze worden gebruikt in paas_oef_2_game.py.
Je kan de code controleren door deze game uit te voeren.
  ! OPGELET: spel zal crashen tot __init__ van Speler opgesteld is !

Je kan het spel opsplitsen in een aantal onderdelen.
Wat volgt is een overzicht van de methoden die je moet ontwikkelen per onderdeel.
    (1) Spel starten:  __init__ Speler.
    (2) Speler beweegt horizontaal: methoden (1) & beweeg_horizntaal.
    (3) Speler beweegt verticaal: methoden (1), raakt_grond & beweeg_verticaal
    (4) Kogels maken & tekenen: methoden (1), __init__ Kogel, schiet_kogel & teken_kogels
    (5) Kogels bewegen & verwijderen: methoden (4), beweeg, reset_kan_klikken, beweeg_kogels & verwijder_kogels.

"""

import pygame, random

class Kogel:
    def __init__(self,x:int,y:int): # (  / 1)
        self.x = x
        self.y = y
        self.kleur = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        self.breedte = 5
        self.hoogte = 20
        """ Geef objecten van Kogel volgende eigenschappen.
          - x: x-positie van de kogel. Neem rechtstreeks over uit de parameter.
          - y: y-positie van de kogel. Neem rechtstreeks over uit de parameter.
          - kleur: kleur van de kogel. Maak deze zelf door 3 random waarden tussen 0-255 te genereren.
          - breedte: breedte van de kogel. Is altijd 5
          - hoogte: hoogte van de kogel. Is altijd 20.
        """


    def beweeg(self, snelheid): # (  / 0.5)
        " Beweeg de kogel omhoog (dus wijzig positie) met de aangegeven snelheid. "
        self.y -= snelheid


    def teken(self, screen:pygame.Surface): # REEDS GEMAAKT.
        " Teken kogel op scherm. "
        pygame.draw.rect(screen, self.kleur, (self.x,self.y,self.breedte,self.hoogte))


class Speler:
    def __init__(self, afb:str, x:int, y:int): # (  / 1.5)
        self.x = x
        self.y = y
        self.kanSpringen = False
        self.ySnelheid = 0
        self.kogels = []
        """ Geef objecten van Speler volgende eigenschappen.
          - afb: afbeelding van de speler. REEDS GEMAAKT.
          - x: x-positie van de speler. Neem rechtstreeks over uit de parameter.
          - y: y-positie van de speler. Neem rechtstreeks over uit de parameter.
          - kan_springen: kan speler springen? Start ALTIJD gelijk aan False.
          - vy: y-snelheid van de speler.      Start altijd gelijk aan 0.
          - kogels: kogels van de speler.      Start altijd als een lege lijst.
        """
        self.afb = pygame.image.load(afb) # REEDS GEMAAKT.


    def beweeg_horizontaal(self, links:bool, rechts:bool, breedte_scherm:int): # (  / 1)
        """ Beweeg speler horizontaal.
        Parameters links & rechts geven aan of q- & d-toets zijn ingedrukt.
        Verlaag de x-positie met 10 als de q-toets is ingedrukt.
        Verlaag de x-positie met 10 als d-toets is ingedrukt.

        De beweging mag niet plaatsvinden als dit de speler uit het scherm beweegt.
        """
        if self.x > 0 and links == True:
            self.x -= 10

        elif self.x + self.afb.get_width() < breedte_scherm and rechts == True:
            self.x += 10

        if self.x < 0:
            self.x = 0

    def raakt_grond(self, hoogte_scherm:int): # (  / 1)
        """ Controleer of speler de grond raakt. 
        Parameter hoogte_scherm geeft de hoogte van het scherm.

        Controleer of de speler onderaan het scherm raakt.
        Indien dit zo is, stel y-snelheid gelijk aan 0 & stel kan_springen gelijk aan True.
        """

        if self.y > hoogte_scherm - self.afb.get_height():
            self.ySnelheid = 0
            self.y = hoogte_scherm - self.afb.get_height()
            self.kanSpringen = True



    def beweeg_verticaal(self, spatie:bool): # (  / 1.5)
        """ Beweeg speler verticaal. 
        Parameter spatie geeft aan of de spatiebalk is ingeduwd.

        Als spatie is ingedrukt en de speler kan springen,
        zet dan vy naar -20 en zet kan_springen naar False.

        Verhoog altijd de y-positie van de speler met zijn y-snelheid.
        Verhoog tenslotte altijd de y-snelheid met 1.
        """

        if spatie and self.kanSpringen:
            self.ySnelheid = -20
            self.kanSpringen = False

        self.ySnelheid += 1
        self.y += self.ySnelheid
            

            



    def schiet_kogel(self, linkermuis:bool): # (  / 1.5)
        """ Is linkermuis ingedrukt? Voeg kogel toe aan lijst.
        De x-positie van de kogel is het midden van de speler.
        De y-positie van de kogel is 10 pixels boven de speler.
        """
        if linkermuis:
            self.kogels.append(Kogel(self.x + (self.afb.get_width() / 2), self.y - 10))

    def teken_kogels(self, screen:pygame.Surface): # (  / 0.5)
        """ Teken iedere kogel in de lijst kogels.
        Gebruik hiervoor de methode teken in Kogel.
        """
        for kogel in self.kogels:
            kogel.teken(screen)


    def beweeg_kogels(self): # (  / 0.5)
        """ Beweeg iedere kogel in de lijst kogels.
        Gebruik hiervoor de methode beweeg in Kogel.
        Iedere kogel moet 5 pixels bewegen
        """
        for kogel in self.kogels:
            kogel.y -= 10

    def verwijder_kogels(self, hoogte_scherm:int): # (  / 1)
        """ Verwijder kogel, als deze uit het scherm verdwijnt. """

        for index, kogel in enumerate(self.kogels):
            if kogel.y < -25:
                self.kogels.pop(index)

    def teken(self, screen:pygame.Surface): # REEDS GEMAAKT.
        " Teken speler op scherm. "
        screen.blit(self.afb, (self.x, self.y))
