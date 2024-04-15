""" OEFENING 2:
Ontwikkel onderstaande klassen. Ze worden gebruikt in oefening_2_game.py.
Je kan de code controleren door deze game uit te voeren.
"""

import pygame
from paas_oef_2 import Speler

# Zet Pygame klaar.
pygame.init()
kleur_achtergrond = (255,255,255)
breedte, hoogte = 800, 600 
screen = pygame.display.set_mode((breedte, hoogte))
klok = pygame.time.Clock()

# Zet alle spelelementen klaar.
speler = Speler(r"pasen_voorbeeldexamen\speler.png",92,117)

running, kan_springen = True, False
while running:
    # Stel spel in op 30 FPS.
    klok.tick(30)
    pygame.event.pump()

    "ACTIE 1: interactie speler."
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False   

    toetsen = pygame.key.get_pressed()
    muis    = pygame.mouse.get_pressed()
    speler.beweeg_horizontaal(toetsen[pygame.K_q], toetsen[pygame.K_d], breedte)
    speler.beweeg_verticaal(toetsen[pygame.K_SPACE])
    speler.schiet_kogel(muis[0])

    "ACTIE 2: spel-staat wijzigen. "
    speler.raakt_grond(hoogte)
    speler.beweeg_kogels()
    speler.verwijder_kogels(hoogte)

    "ACTIE 3: teken op scherm."
    screen.fill(kleur_achtergrond) # Reset scherm
    speler.teken(screen)
    speler.teken_kogels(screen)

    pygame.display.flip() # Toon scherm aan speler.