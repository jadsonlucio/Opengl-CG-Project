from .vectors import Vector3D
import numpy as np

class Particle():
    def __init__(self, x, y, z, weight, elasticity, speed, acceleration):
        self._pos = np.array([x,y,z])
        self.weight = weight
        self.elasticity = elasticity
        self.elasticity = elasticity
        self.acceleration = acceleration
        self.movement_vectors = []

    def add_movement_vector(self, movement_vector):
        if isinstance(movement_vector, list):
            movement_vector = Vector3D(*movement_vector)
        
        self.movement_vectors.append(movement_vector)
        
    def move(self, time_frame):
        for mov_vec in self.movement_vectors:
            self.pos += mov_vec.norm_direction * mov_vec.intencity * time_frame

    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, pos):
        self._pos = pos

    