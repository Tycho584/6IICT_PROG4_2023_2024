""" --------------- Benodigde modules --------------- """  
import copy
import random
import pygame

HOOGTE = 200
BREEDTE = 200

CEL_HOOGTE = 5
CEL_BREEDTE = 5

KANS_LEVEND = 0.1

def maak_dood_bord(hoogte, breedte):
    bord = []
    for hoog in range(hoogte):
        rij =[0]*breedte
        bord.append(rij)



    return bord

"""
[ 
  [0, 0],
  [0, 0]
]
""" 
print( maak_dood_bord(2,2) ) 

def bord_start_staat(bord, kans_levend):
    for rij, rijwaarde in enumerate(bord):
        for kollom, kollomwaarde in enumerate(rijwaarde):
            kans = random.random()
            if kans <= kans_levend:
                bord[rij][kollom ] = 1
            elif kans > kans_levend:
                bord[rij][kollom] = 0
            
    return bord

def get_buur_links(bord, y, x):
    if x == 0:
        linker_buur_waarde = 0
    else:
        linker_buur_waarde = bord[y][x - 1]

    return linker_buur_waarde

def get_buur_rechts(bord, y, x):
    rechter_grens = len(bord[0]) - 1
    if x == rechter_grens:
        rechter_buur_waarde = 0
    else:
        rechter_buur_waarde = bord[y][x + 1]
    return rechter_buur_waarde

def get_buur_boven(bord, y, x):
    if y == 0:
        boven_buur_waarde = 0
    else:
        boven_buur_waarde = bord[y-1][x]
    return boven_buur_waarde

def get_buur_onder(bord, y, x):
    onder_grens = len(bord[0]) - 1
    if y == onder_grens:
        onder_buur_waarde = 0
    else:
        onder_buur_waarde = bord[y + 1][x]
    return onder_buur_waarde

def get_buur_linksboven(bord, y, x):
    if y == 0 or x == 0:
        linkerboven_buur_waarde = 0
    else:
        linkerboven_buur_waarde = bord[y -1][x - 1]
    return linkerboven_buur_waarde

def get_buur_rechtsboven(bord, y, x):
    rechter_grens = len(bord[0]) - 1
    if y == 0 or x == rechter_grens:
        rechterboven_buur_waarde = 0
    else:
        rechterboven_buur_waarde = bord[y - 1][x + 1]
    return rechterboven_buur_waarde

def get_buur_linksonder(bord, y, x):
    onder_grens = len(bord[0]) - 1
    if y == onder_grens or x == 0:
        linkeronder_buur_waarde = 0
    else:
        linkeronder_buur_waarde = bord[y + 1][x - 1]
    return linkeronder_buur_waarde

def get_buur_rechtsonder(bord, y, x):
    onder_grens = len(bord[0]) - 1
    rechter_grens = len(bord[0]) - 1
    if y == onder_grens or x == rechter_grens:
        rechteronder_buur_waarde = 0
    else:
        rechteronder_buur_waarde = bord[y + 1][x + 1]
    return rechteronder_buur_waarde


def tel_levende_buren(bord, y, x):
    aantal_levenden = get_buur_boven(bord, y ,x) + get_buur_onder(bord, y, x) + get_buur_links(bord, y, x) + get_buur_rechts(bord, y, x) + get_buur_linksboven(bord, y, x) + get_buur_rechtsboven(bord, y, x) + get_buur_linksonder(bord, y, x) + get_buur_rechtsonder(bord, y, x)
    
    return aantal_levenden


def regels_game_of_life(bord, y, x):
    levend = bord[y][x]
    aantal_levenden = tel_levende_buren(bord, y, x)
    if levend == 1:
        if aantal_levenden == 2 or aantal_levenden == 3:
            leven = True
        else: 
            leven = False
    elif levend == 0:
        if aantal_levenden == 3:
            leven = True
        else:
            leven = False
    return leven

def update_bord(bord):
    """ Update het bord volgens de regels van Game of Life """
    huidig_bord = copy.deepcopy(bord)

    for y, rij in enumerate(huidig_bord):
        for x, _ in enumerate(rij):
            leeft = regels_game_of_life(huidig_bord, y, x)
            if leeft:
                bord[y][x] = 1
            else:
                bord[y][x] = 0

""" --------------- game-loop --------------- """
def main():
    teller = 0
    if teller == 0:
        snelheid = 10
        teller += 1

    pygame.init()
    screen = pygame.display.set_mode((BREEDTE * CEL_HOOGTE, HOOGTE * CEL_HOOGTE))
    clock = pygame.time.Clock()

    bord = maak_dood_bord(HOOGTE, BREEDTE)
    bord_start_staat(bord, KANS_LEVEND)

    running = True
    while running:
        screen.fill((0, 0, 0))
        for y, rij in enumerate(bord):
            for x, cel in enumerate(rij):
                if cel:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x * CEL_BREEDTE,
                        y * CEL_HOOGTE,
                        CEL_BREEDTE,
                        CEL_HOOGTE,
                    ),
                )

        update_bord(bord)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEWHEEL:
                if snelheid <= 90:
                    snelheid *= 10
                elif snelheid == 100:
                    snelheid = 1
        clock.tick(snelheid)


if __name__ == "__main__":
    main()