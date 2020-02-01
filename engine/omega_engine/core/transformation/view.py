import glm
import numpy as np

class View():
    def __init__(self, pos, target_pos = (0.0, 0.0, 0.0), camera_up = (0.0, 1.0, 0.0)):
        self.pos = pos
        self.target_pos = target_pos
        self.camera_up = camera_up
        self.lock_at()
        

    @property
    def matrix4(self):
        return np.array(self._matrix)


    def move(self, x, y, z):
        self.pos = (x, y, z)
        self.lock_at()

    def translate(self, x, y, z):
        self._matrix = glm.translate(self._matrix, glm.vec3(x, y, z))


    def rotate(self, angle, x, y, z):
        self._matrix = glm.rotate(self._matrix, glm.radians(angle), glm.vec3(x, y, z))

    def lock_at(self):
        self._matrix = glm.lookAt(glm.vec3(*self.pos), glm.vec3(*self.target_pos), glm.vec3(*self.camera_up))


    def load_identity(self):
        self._matrix = glm.mat4(1.0)