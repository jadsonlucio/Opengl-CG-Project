import math
from .camera import Camera

class Camera3RDPerson(Camera):
    def __init__(self, entity, x_angle, y_angle, z_angle, camera_height, camera_distance):
        super().__init__([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0, 1, 0])
        self.entity = entity
        self.x_angle = x_angle
        self.y_angle = y_angle
        self.z_angle = z_angle
        self.camera_height = camera_height
        self.camera_distance = camera_distance

        self.update()
        

    def get_camera_pos(self):
        camera_y_d = math.sin(math.radians(self.y_angle)) * self.camera_distance
        camera_distance_xy = math.cos(math.radians(self.y_angle)) * self.camera_distance

        camera_x_d = math.sin(math.radians(self.x_angle)) * camera_distance_xy
        camera_z_d = math.cos(math.radians(self.x_angle)) * camera_distance_xy

        camera_x = self.entity.model.pos[0] - camera_x_d
        camera_y = self.entity.model.pos[1] - camera_y_d
        camera_z = self.entity.model.pos[2] - camera_z_d

        return camera_x, camera_y, camera_z

    def get_camera_target_pos(self):
        return self.entity.model.pos

    
    def update(self):
        self.pos = self.get_camera_pos()
        self.target_pos = self.get_camera_target_pos()
    
    @property
    def matrix4(self):
        self.update()
        self.lock_at()

        return super().matrix4