from OpenGL.GL import *
from map import Map
from opengl_core.pygame_window import Window

class Game(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        self.map = Map()

    def render(self):
        self.map.clock.tick(60)
        self.map.update_camera()
        self.map.sun.model.rotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.map.renderer.draw(self.map.map_obj, self.map.ship.ship_obj)
        self.map.renderer_1.draw(self.map.cube_obj)

    
    def on_key_press(self, event):
        if event.key == 273:
            self.map.ship.move()
        elif event.key == 276:
            self.map.ship.rotate(1)
        elif event.key == 275:
            self.map.ship.rotate(-1)
        """elif event.key == 280:
            self.map.ship.move(0, 0.1, 0)
        elif event.key == 281:
            self.map.ship.move(0, -0.1, 0)"""


    def on_mouse_up(self, event):
        if event.button == 1: self.map.rotate = False
        elif event.button == 3: self.map.move = False
    
    def on_mouse_down(self, event):
        if event.button == 4: self.map.zpos = max(1, self.map.zpos-1)
        elif event.button == 5: self.map.zpos += 1
        elif event.button == 1: self.map.rotate = True
        elif event.button == 3: self.map.move = True


    def on_mouse_motion(self, event):
        i, j = event.rel
        if self.map.rotate:
            self.map.rx += i/100
            self.map.ry += j/100
        if self.map.move:
            self.map.tx += i
            self.map.ty -= j

    def on_resize(self, event):
        self.map.projection.update(width=event.w, height=event.h)

    





