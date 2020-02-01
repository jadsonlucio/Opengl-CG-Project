import numpy as np

class Vector3D:
    def __init__(self, x_dir, y_dir, z_dir, intencity = 1):
        self.vec3 = np.array([x_dir, y_dir, z_dir])
        self.norm_direction = self.vec3 / sum(self.vec3 ** 2) ** 0.5
