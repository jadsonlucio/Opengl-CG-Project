import sys

from inspect import isfunction
from .canvas import Canvas
from .rect import Rect

from .event.event import Events

class Widget(Canvas, Events):
    def __init__(self, master, posX, posY, width, height):
        self.master = master
        self.children = []

        master_rect = None
        if master != None and isinstance(master, Widget):
            master_rect = master.rect
            self.master.children.append(self)

        self.rect = Rect(master_rect, posX, posY, width, height)
        Canvas.__init__(self, width, height)
        Events.__init__(self)

        self._on_init()

    def on_init(self):
        pass

    def on_render(self):
        self.master.blit(self, self.rect.relpos())

    def on_loop(self):
        pass
        
    def resize(self):
        pass

    def _update(self, events):
        events = self.process_events(events)
        class_list = self.__class__.mro()
        class_list.reverse()
        for class_obj in class_list:
            if issubclass(class_obj, Widget):
                class_obj.on_loop(self)
                class_obj.on_render(self)

        for child in self.children:
            if isinstance(child, Widget):
                child._update(events)

    def _on_init(self):
        for class_obj in self.__class__.mro():
            if issubclass(class_obj, Widget):
                class_obj.on_init(self)




