import pygame
from .event.event import Events
from .event.custom_events import set_custom_events

class Window(Events):
    def __init__(self, title, width, height, mode):
        self.__running = False
        self.title = title 
        self.__display_surf = pygame.display.set_mode((width, height), mode)

        Events.__init__(self)

    def on_execute(self):
        self.__running = True
        self.on_init()
        while(self.__running):
            set_custom_events()
            events = pygame.event.get()
            self._update(events)

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.__running = False

    def on_cleanup(self):
        pygame.quit()

    def on_init(self):
        pygame.init()
    
    def on_render(self):
        pygame.display.flip()

    def _update(self, events):
        events = self.process_events(events)
        self.on_render()