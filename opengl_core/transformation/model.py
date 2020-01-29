import glm
import numpy as np

class MatrixModel():
    def __init__(self, matrix = None):
        if matrix == None:
            matrix = glm.mat4(1.0)
        
        self.__matrix = matrix

    
    def rotate(self, angle, x, y, z):
        self.__matrix = glm.rotate(self.__matrix, glm.radians(angle), glm.vec3(x, y, z))
    

    def translate(self, x, y, z):
        self.__matrix = glm.translate(self.__matrix, glm.vec3(x, y, z))

    def scale(self, x_scale, y_scale, z_scale):
        self.__matrix = glm.scale(self.__matrix, glm.vec3(x_scale, y_scale, z_scale))

    def multiply(self, matrix4):
        self.__matrix =  glm.dot(matrix4, self.__matrix)

    @property
    def pos(self):
        return glm.vec3(glm.column(self.__matrix, 3))

    @pos.setter
    def pos(self, new_pos):
        self.__matrix = glm.column(self.__matrix, 3, glm.vec4(*new_pos, 1.0))

    @property
    def matrix4(self):
        return np.array(self.__matrix)