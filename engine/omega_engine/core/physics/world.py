from .vectors import Vector3D
from .physical_constants import EARTH_GRAVITY_MS_2

class World():
    def __init__(self, pixel_meter_density, gravity = EARTH_GRAVITY_MS_2):
        self.gravity = gravity
        self.pixel_meter_density = pixel_meter_density
        self._particles = []
        self._vectors = None

    def inicialize_vectors(self):
        self._vectors = []
        self._vectors.append(Vector3D(0, 1, 0, self.gravity))

    def add_particle(self, particle):
        self._particles.append()

    def move_particles(self):
        pass
    