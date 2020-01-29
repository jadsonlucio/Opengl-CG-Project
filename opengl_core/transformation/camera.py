import glm
import numpy as np

class Camera():
    def __init__(self, pos, target_pos = (0.0, 0.0, 0.0), camera_up = (0.0, 1.0, 0.0)):
        self.pos = pos
        self.target_pos = target_pos
        self.camera_up = camera_up
        self._set_camera_matrix()
        

    @property
    def matrix4(self):
        return np.array(self._matrix)


    def move(self, x, y, z):
        self.pos = (x, y, z)
        self._set_camera_matrix()

    def translate(self, x, y, z):
        self._matrix = glm.translate(self._matrix, glm.vec3(x, y, z))


    def rotate(self, angle, x, y, z):
        self._matrix = glm.rotate(self._matrix, angle, glm.vec3(x, y, z))

    def _set_camera_matrix(self):
        self._matrix = glm.lookAt(glm.vec3(*self.pos), glm.vec3(*self.target_pos), glm.vec3(*self.camera_up))


    def load_identity(self):
        self._matrix = glm.mat4(1.0)