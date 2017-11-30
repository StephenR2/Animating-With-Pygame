import pygame
class Brick:


    def __init__(self, surface, height, width, color):
        self.surface = surface
        self.height = height
        self.width = width
        self.color = color
        pygame.init()
    def draw(self, x, y):
        pygame.draw.rect(self.surface, self.color, (x , y, self.width, self.height), 0)

