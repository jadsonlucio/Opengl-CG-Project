import os
import pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,60'

class Window():
    def __init__(self, screen_name, width, height):
        self.screen_name = screen_name
        self.width = width
        self.height = height
        self.executing = False

        pygame.init()
        pygame.display.set_mode((self.width, self.height), pygame.OPENGL|pygame.DOUBLEBUF|pygame.RESIZABLE)

    def render(self):
        pass

    def on_key_press(self, event):
        pass

    def on_mouse_up(self, event):
        pass

    def on_mouse_down(self, event):
        pass


    def on_mouse_motion(self, event):
        pass

    def on_resize(self, event):
        pass

    def execute(self):
        self.executing = True

        while self.executing:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.executing = False
                elif event.type == pygame.KEYDOWN:
                    self.on_key_press(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.on_mouse_up(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_mouse_down(event)
                elif event.type == pygame.MOUSEMOTION:
                    self.on_mouse_motion(event)
                elif event.type == pygame.VIDEORESIZE:
                    self.on_resize(event)
            
            ct = pygame.time.get_ticks() / 1000
            self.render()

            pygame.display.flip()
        
        pygame.quit()