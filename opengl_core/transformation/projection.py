import glm
import numpy as np
from OpenGL.GL import glViewport

class Projection():
    def __init__(self, field_view ,width, height, znear, zfar):
        self.field_view = field_view
        self.width = width
        self.height = height
        self.znear = znear
        self.zfar = zfar

        glViewport(0, 0, width, height)
        self.__matrix = glm.perspective(field_view, width/height, znear, zfar)

    @property
    def matrix4(self):
        return np.array(self.__matrix)


    def update(self, field_view = None, width = None, 
                height = None, znear = None, zfar = None):
        if field_view != None:
            self.field_view = field_view
        if width != None:
            self.width = width
        if height != None:
            self.height = height
        if znear != None:
            self.znear = znear
        if zfar != None:
            self.zfar = zfar

        glViewport(0, 0, self.width, self.height)
        self.__matrix = glm.perspective(self.field_view, 
                self.width/self.height, self.znear, self.zfar)
        