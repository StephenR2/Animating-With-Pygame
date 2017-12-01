import pygame
class Brick:


    def __init__(self, surface, height, width, color):
        """
        Initializing stating the parameters it needs
        :param surface: The surface
        :param height: Height of the brick
        :param width: Width of the brick
        :param color: Color of the brick
        """
        self.surface = surface
        self.height = height
        self.width = width
        self.color = color
        pygame.init()
    def draw(self, x, y):
        """
        Method used to actually draw the brick that it has made.
        :param x: x coord, parameter that draw needs to know in order to draw.
        :param y: y coord, parameter that draw needs to know in order to draw
        :return: Returns a drawn brick in the position specified.
        """
        pygame.draw.rect(self.surface, self.color, (x , y, self.width, self.height), 0)

