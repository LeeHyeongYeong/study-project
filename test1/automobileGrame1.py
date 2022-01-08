import pygame
import sys
from time import sleep
padWidth = 480
padHeight = 800

WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

def initGame():
    global gamePad, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    
    background = pygame.image.load('background.png')
    fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    clock = pygame.time.Clock()


def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def runGame():
    global gamePad, clock, background, fighter, missile, explosion
    onGame = False

    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        drawObject(background, 0, 0)
        pygame.display.update()
        clock.tick(60)
    clock.quit()


       


initGame()
runGame()



