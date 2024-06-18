import os, cv2

""" Niveau 1
Tip! ALS de instructie IN de afbeeldingsnaam staat. Voer dan de instructie uit.
"""


""" Niveau 2
Tip! Hou bij in welke map(pen) de uiteindelijke afbeelding opgeslagen moet worden.
"""


""" Niveau 3
Tip! Er worden _ gebruikt om de verschillende instructies te scheiden.
Tip! Als je dit goed doet, zouden afb4 en afb5 elkaars spiegelbeeld moeten zijn.
"""
folder_pad    = "Examens\oefening2\src"
folder_inhoud = os.listdir(folder_pad) 

# Overloop alle afbeeldingen in folder.
teller = 0
for index, bestand in enumerate(folder_inhoud):
    if (".png" in bestand) or (".jpg" in bestand): # We werken enkel met png- of jpg-bestanden.
        teller = teller + 1
        print(f"Bestand {teller}: {bestand}")

        bestand_pad    = f"{folder_pad}/{bestand}"
        naam, extensie = os.path.splitext(bestand)
        afbeelding     = cv2.imread(bestand_pad) 

        if "rot90" in bestand:
            image90Rotated = cv2.rotate(afbeelding, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(filename=f"{folder_pad}/result1/{naam}.{extensie}", img=image90Rotated)

        if "rot-90" in bestand:
            imageCounter90Rotated = cv2.rotate(afbeelding, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(filename=f"{folder_pad}/result1/{naam}.{extensie}", img=imageCounter90Rotated)
        
        if "flipV" in bestand:
            imageMirrored = cv2.flip(afbeelding, 0)
            cv2.imwrite(filename=f"{folder_pad}/result1/{naam}_gespiegeld_.{extensie}", img=imageMirrored)

        if "flipH" in bestand:
            imageMirrored = cv2.flip(afbeelding, 1)
            cv2.imwrite(filename=f"{folder_pad}/result1/{naam}_gespiegeld_.{extensie}", img=imageMirrored)

        if "blur" in bestand:
            imageBlurred =  cv2.blur(afbeelding,(20,20))
            cv2.imwrite(filename=f"{folder_pad}/result1/{naam}_blurred_.{extensie}", img=imageBlurred)