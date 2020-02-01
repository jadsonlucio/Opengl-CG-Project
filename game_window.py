import pygame
from OpenGL.GL import *
from map import Map
from omega_engine.window.pygameAPI.windows.opengl_window import OpenglWindow

class GameWindow(OpenglWindow):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.map = Map()
    
    def on_render(self):
        self.map.clock.tick(60)
        self.map.update_camera()
        self.map.sun.model.rotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.map.renderer.draw(self.map, self.map.ship)
        self.map.renderer_1.draw(self.map.sun, self.map.sky)

        pygame.display.flip()

    def key_pressed(self, event):
        if event.key == 32:
            self.map.camera.selected_cam = not self.map.camera._index

    def key_hold(self, event):
        if event.key == 273:
            self.map.ship.move()
        elif event.key == 97:
            self.map.ship.rotate(y_angle = 0.3)
        elif event.key == 100:
            self.map.ship.rotate(y_angle = -0.3)
        elif event.key == 119:
            self.map.ship.rotate(x_angle = -0.3)
        elif event.key == 115:
            self.map.ship.rotate(x_angle = 0.3)
        elif event.key == 113:
            self.map.ship.rotate(z_angle = -0.3)
        elif event.key == 101:
            self.map.ship.rotate(z_angle = 0.3)
        elif event.key == 280:
            self.map.ship.fly(1)
        elif event.key == 281:
            self.map.ship.fly(-1)

        print(event)
    
    def key_down(self, event):
        if event.key == 273:
            pygame.mixer.music.load('resources/songs/Cabin.wav')
            pygame.mixer.music.play(-1)
    
    def key_up(self, event):
        if event.key == 273:
            pygame.mixer.music.stop()

    def mouse_up(self, event):
        if event.button == 1: self.map.rotate = False
        elif event.button == 3: self.map.move = False
    
    def mouse_down(self, event):
        if event.button == 4: self.map.zpos = max(1, self.map.zpos-1)
        elif event.button == 5: self.map.zpos += 1
        elif event.button == 1: self.map.rotate = True
        elif event.button == 3: self.map.move = True

    def mouse_moved(self, event):
        i, j = event.rel
        if self.map.camera.selected_cam == self.map.world_camera:
            if self.map.rotate:
                self.map.rx += j/2
                self.map.ry += i/2
            if self.map.move:
                self.map.tx += i
                self.map.ty -= j

    
    def window_resize(self, event):
        self.map.projection.update(width=event.w, height=event.h)

    