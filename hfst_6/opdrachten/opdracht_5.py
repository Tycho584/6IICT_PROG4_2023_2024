import pygame, time
 
# Kleuren
ZWART = (0, 0, 0)
WIT   = (255, 255, 255)

""" 
(TODO) Recursieve rechthoek functie.
Het tekenen van rechthoeken op het scherm kan als volgt: 
pygame.draw.rect(scherm, ZWART, [x, y, breedte, hoogte],1)
"""
def recursieve_rechthoek(x, y, breedte, hoogte, scherm):
    if breedte < 10 or hoogte < 10:
        return
    
    recursieve_rechthoek(x+(0.1*breedte), y+(0.1*hoogte), breedte * 0.8, hoogte * 0.8, scherm)
    pygame.draw.rect(scherm, ZWART, pygame.Rect(x, y, breedte, hoogte), 1)

""" 
Functie reeds voltooid.
Open pygame scherm met instellingen voor rechthoek. 
"""
def main():
    # Instellingen
    running = True
    breedte, hoogte = 700, 500
    pygame.init()
    scherm = pygame.display.set_mode([breedte, hoogte])
    pygame.display.set_caption("Recursieve rechthoek")
    clock = pygame.time.Clock()

    # -------- Main Loop -----------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        scherm.fill(WIT)
    
        """ Teken rechthoeken zoals aangegeven op GitHub. """
        recursieve_rechthoek(0, 0, breedte, hoogte, scherm)
    
        pygame.display.flip()
        clock.tick(60)
    
    # Stop pygame
    pygame.quit()

if __name__ == "__main__":
    main()