import numpy as np
from ...transformation.view import View


class Camera(View):
    def __init__(self, pos, target_pos=(0, 0, 0), camera_up=(0, 1, 0)):
        super().__init__(pos, target_pos, camera_up)

    def save(self, file_path):
        np.save(file_path, self.matrix4)

    @staticmethod
    def load(file_path):
        matrix = np.load(file_path)
        camera = Camera((0, 0, 0))
        camera._matrix = matrix

        return camera