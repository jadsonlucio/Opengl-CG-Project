import pygame

clock = pygame.time.Clock()

class Window():
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.title)

    def run(self):
        pygame.display.flip()
        clock.tick(60)

    
    def render(self):
        raise NotImplementedError()
        




