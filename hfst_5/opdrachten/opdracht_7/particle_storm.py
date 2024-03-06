# Vul de TODO's aan op basis van de uitleg in de README.

import pygame, random
from particle import BoringParticle, BouncingParticle, SpinningParticle

# Constantes.
BREEDTE, HOOGTE = 1200,600
VORIGE_BREEDTE, VORIGE_HOOGTE = BREEDTE, HOOGTE
FPS = 120
AANTAL_BORING_PARTICLES = 30
AANTAL_BOUNCING_PARTICLES = 30
AANTAL_SPINNING_PARTICLES = 30
BORING_KLEUR = [[255,255,255]]
BOUNCING_KLEUR = [[255,255,0],[0,0,255]]
SPINNING_KLEUR = [[255,0,0],[0,255,0]]

# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((BREEDTE,HOOGTE), pygame.RESIZABLE)
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* aan met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.

boringParticles = []  
bouncingParticles = []
spinningParticles = []

for particle in range(AANTAL_BORING_PARTICLES):
    particleKleur = random.choice(BORING_KLEUR)
    boringParticles.append(BoringParticle(10, BREEDTE/2, HOOGTE/2, particleKleur))

for particle in range(AANTAL_BOUNCING_PARTICLES):
    particleKleur = random.choice(BOUNCING_KLEUR)
    bouncingParticles.append(BouncingParticle(10, BREEDTE/2, HOOGTE/2, particleKleur))

for particle in range(AANTAL_SPINNING_PARTICLES):
    particleKleur = random.choice(SPINNING_KLEUR)
    spinningParticles.append(SpinningParticle(10, BREEDTE/2, HOOGTE/2, particleKleur))
    
    
running = True
while running:
    BREEDTE, HOOGTE = scherm.get_size()
    # Maak scherm schoon.
    scherm.fill((48,48,48))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(FPS)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    for particle in boringParticles:
        particle.updatePosition(interval)
        particle.reset(BREEDTE, HOOGTE)
        pygame.draw.circle(scherm, particle.color, (particle.XCoordinate, particle.YCoordinate), particle.radius)

    for particle in bouncingParticles:
        particle.updatePosition(interval)
        particle.bounceOfHorizontalWall(HOOGTE,BREEDTE)
        particle.bounceOfVerticalWall(HOOGTE,BREEDTE)
        pygame.draw.circle(scherm, particle.color, (particle.XCoordinate, particle.YCoordinate), particle.radius)

    for particle in spinningParticles:
        particle.updatePosition(interval)
        pygame.draw.circle(scherm, particle.color,(particle.XCoordinate, particle.YCoordinate),particle.radius)

    # Toon scherm aan gebruiker.
    if BREEDTE != VORIGE_BREEDTE or HOOGTE != VORIGE_HOOGTE:
        for particle in boringParticles:
            particle.resetByResize(BREEDTE, HOOGTE)
            pygame.draw.circle(scherm, particle.color, (particle.XCoordinate, particle.YCoordinate), particle.radius)

        for particle in bouncingParticles:
            particle.resetByResize(BREEDTE,HOOGTE)
            pygame.draw.circle(scherm, particle.color, (particle.XCoordinate, particle.YCoordinate), particle.radius)
            
        for particle in spinningParticles:
            particle.resetByResize(BREEDTE,HOOGTE)
            pygame.draw.circle(scherm, particle.color, (particle.XCoordinate, particle.YCoordinate), particle.radius)

    VORIGE_HOOGTE = HOOGTE
    VORIGE_BREEDTE = BREEDTE

    pygame.display.update()

pygame.quit()