# Stephen Randall
# 11/30/17
# Folder: Unit10Project File: diagram.py
# This is a simple program that uses pygame to draw a breaker game layout.
import brick
import pygame
import sys
from pygame.locals import *

pygame.init()

mainSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Brick Display")
# Constants , information that doesn't change has a variable name with all caps.
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
WHITESPACE = 5
NUMBRICKS = 9
SCRWIDTH = mainSurface.get_width()
mainSurface.fill(WHITE)
WIDTHSTEPONE = (WHITESPACE * NUMBRICKS - WHITESPACE)
WIDTH = (SCRWIDTH - WIDTHSTEPONE) / NUMBRICKS
brickX = 0
brickY = 380
for x in range(9):  # Draw bottom layer of bricks
    brickOne = brick.Brick(mainSurface, 20, WIDTH, RED)
    brickOne.draw(brickX, brickY)
    brickX = brickX + WIDTH + WHITESPACE  # Redefining x coordinate for where the next brick will be drawn.
brickY = 360 - WHITESPACE  # Redefining the y coord for the next layer of bricks
brickX = WIDTH + WHITESPACE  # Redefining the x coord for the next layer of bricks
for a in range(7):
    brickTwo = brick.Brick(mainSurface, 20, WIDTH, PINK)
    brickTwo.draw(brickX, brickY)
    brickX = brickX + WIDTH + WHITESPACE
brickY = 340 - (2 * WHITESPACE)

brickX = (2 * WIDTH) + (2 * WHITESPACE)
for c in range(5):
    brickThree = brick.Brick(mainSurface, 20, WIDTH, BLUE)
    brickThree.draw(brickX, brickY)
    brickX = brickX + WIDTH + WHITESPACE
brickY = 320 - (3 * WHITESPACE)
brickX = (3 * WIDTH) + (3 * WHITESPACE)
for b in range(3):
    brickFour = brick.Brick(mainSurface, 20, WIDTH, GREEN)
    brickFour.draw(brickX, brickY)
    brickX = brickX + WIDTH + WHITESPACE
brickY = 300 - (4 * WHITESPACE)
brickX = (4 * WIDTH) + (4 * WHITESPACE)
for h in range(1):
    brickFive = brick.Brick(mainSurface, 20, WIDTH, BLACK)
    brickFive.draw(brickX, brickY)
    brickX = brickX + WIDTH + WHITESPACE

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
