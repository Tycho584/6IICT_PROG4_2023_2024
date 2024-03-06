import pygame

class Game:
    def __init__(self, width: int, height: int, captionName: str, FPS: int) -> None:
        self.width = width
        self.height = height
        self.captionName = captionName
        self.FPS = FPS

        self.player = Player()

    def createScreen(self):
        self.screen = pygame.display.set_mode(self.width, self.height)


    def drawScreen(self):
        Player.spawningPlayer(self.screen)

class Background(Game):

    def __init__(self, backgroundPicture: str, backgroundColor: list) -> None:
        super().__init__()
        self.backgroundPicture = backgroundPicture
        self.backgroundColor = backgroundColor

    def setBackground(self):
        if self.backgroundPicture != "":
           background = pygame.image.load(self.backgroundPicture)
        else:
            color = (self.backgroundColor)
            
class Player():
    def __init__(self, playerXPostion, playerYPosition, playerSpeed) -> None:
        self.playerXPostion = playerXPostion
        self.playerYPosition = playerYPosition
        self.playerSpeed = playerSpeed

    def spawningPlayer(self, screen):
        screen.blit()

    def playerPositioning(self):
        pass