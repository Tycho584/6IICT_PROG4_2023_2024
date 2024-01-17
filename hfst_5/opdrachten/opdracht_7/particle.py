# Voeg eigenschappen / methoden toe aan BoringParticle op basis van de uitleg in de README.
import random, math

class BoringParticle:
    def __init__(self, radius, XCoordinate, YCoordinate, color) -> None:
        self.radius = radius
        self.generateSpeed()
        self.XCoordinate = XCoordinate
        self.YCoordinate = YCoordinate
        self.color = color
    
    def updatePosition(self, interval):
        self.XCoordinate += self.XSpeed * interval
        self.YCoordinate += self.YSpeed * interval

    def reset(self, BREEDTE, HOOGTE):
            if self.XCoordinate < 0 or self.XCoordinate > BREEDTE or self.YCoordinate < 0 or self.YCoordinate > BREEDTE:
                self.XCoordinate, self.YCoordinate = BREEDTE/2, HOOGTE/2
                self.generateSpeed()

    def generateSpeed(self):
        self.XSpeed = random.random() - 0.5
        self.YSpeed = random.random() - 0.5


class BouncingParticle:
    def __init__(self, radius, XCoordinate, YCoordinate, color) -> None:
        self.radius = radius
        self.generateSpeed()
        self.XCoordinate = XCoordinate
        self.YCoordinate = YCoordinate
        self.color = color

    def changeColor(self):
        if self.color == [255,255,0]:
            self.color = [0,0,255]
        else:
            self.color = [255,255,0]

    def updatePosition(self, interval):
        self.XCoordinate += self.XSpeed * interval
        self.YCoordinate += self.YSpeed * interval

    def generateSpeed(self):
        self.XSpeed = random.random() - 0.5
        self.YSpeed = random.random() - 0.5

    def bounceOfHorizontalWall(self, HOOGTE, BREEDTE):
        if self.XCoordinate < 0 or self.XCoordinate > BREEDTE:
            self.XSpeed = -self.XSpeed
            self.changeColor()
            self.generateSpeed

    def bounceOfVerticalWall(self, HOOGTE, BREEDTE):
        if self.YCoordinate < 0 or self.YCoordinate > HOOGTE:
            self.YSpeed = -self.YSpeed
            self.changeColor()
            self.generateSpeed


class SpinningParticle:

    def __init__(self, radius, XCoordinate, YCoordinate,color) -> None:
        self.radius = radius
        self.generateSpeed()
        self.XCoordinate = XCoordinate
        self.YCoordinate = YCoordinate
        self.color = color

    def generateSpeed(self):
        self.Speed = random.random() - 0.5
        self.angle = random.random() * (2 * math.pi)

    def updatePosition(self,interval):
        self.angle += (random.random() * 0.01) * math.pi
        self.XCoordinate += self.Speed * math.cos(self.angle) * interval
        self.YCoordinate += self.Speed * math.sin(self.angle) * interval