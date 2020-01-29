import pygame
from ..widget.window import Window

class OpenglWindow(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height, pygame.OPENGL|pygame.DOUBLEBUF|pygame.RESIZABLE)