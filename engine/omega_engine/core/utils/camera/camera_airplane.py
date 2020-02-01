import math
import glm
import numpy as np
from .camera import Camera

class CameraAirPlane(Camera):
    def __init__(self, entity, camera_height, camera_distance):
        self.entity = entity
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0
        self.camera_height = camera_height
        self.camera_distance = camera_distance

        super().__init__((0,0,9), target_pos = self.entity.model.pos)
        
    def rotate(self, x_angle = 0, y_angle = 0, z_angle = 0):
        self.x_angle += x_angle
        self.y_angle += y_angle
        self.z_angle += z_angle

    def get_camera_target_pos(self):
        return self.entity.model.pos
    
    def get_camera_pos(self):
        x, y, z = self.entity.model.pos
        cam_x, cam_y, cam_z, _ = np.dot(np.array(self.entity.model.matrix4).transpose(),
                                     np.array(glm.vec4(0, self.camera_height, -self.camera_distance, 1)))

        return cam_x, cam_y, cam_z

    def update(self):
        self.pos = self.get_camera_pos()
        self.target_pos = self.get_camera_target_pos()
    
    @property
    def matrix4(self):
        self.update()
        self.lock_at()

        return super().matrix4