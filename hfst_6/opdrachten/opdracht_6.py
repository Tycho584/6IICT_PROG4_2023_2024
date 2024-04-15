import pygame
 
# Colors
ZWART = (0, 0, 0)
WIT = (255, 255, 255)
 
""" 
(TODO) Recursieve fractaal functie.
Het tekenen van 'H' op het scherm gebeurt als volgt:
teken_h(x, y, breedte, hoogte, scherm)

Fractalen tekenen moet stoppen na een bepaalde max_diepte te bereiken.
De diepte begint best bij 0 en verhoogd met 1, telkens wanneer je een kleinere fractaal tekent.
"""
def recursieve_fractaal(x, y, width, height, maxDepth, currentDepth, screen):
    drawH(x,y,width,height,screen)

 
""" Teken een H op een bepaalde positie (x,y) & een bepaalde grootte (breedte,hoogte). """
def drawH(x,y,width,height, screen):
    pygame.draw.line(screen,
                    ZWART,
                    [x + width*.25, height // 2 + y],
                    [x + width*.75, height // 2 + y],
                    3)
    pygame.draw.line(screen,
                    ZWART,
                    [x + width * .25, (height * .5) // 2 + y],
                    [x + width * .25,  (height * 1.5) // 2 + y],
                    3)
    pygame.draw.line(screen,
                    ZWART,
                    [x + width * .75, (height * .5) // 2 + y],
                    [x + width * .75, (height * 1.5) // 2 + y],
                    3)

""" Open pygame scherm met instellingen voor rechthoek.  """
def main(): 
    # Instellingen 
    running = True
    width, height = 700, 700
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    
    # -------- Main Loop -----------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(WIT)

        """ Teken fractalen zoals aangeven op GitHub. """
        maxDepth = 3
        currentDepth = 0
        recursieve_fractaal(0, 0, width, height, maxDepth, currentDepth, screen)
    
        pygame.display.flip()
        clock.tick(20)
    
    pygame.quit()

if __name__ == "__main__":
    main()