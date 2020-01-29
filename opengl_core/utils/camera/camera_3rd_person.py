import math
from ...transformation.camera import Camera

class Camera3RDPerson(Camera):
    def __init__(self, entity, entity_angle, camera_height, camera_distance):
        super().__init__([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0, 1, 0])
        self.entity = entity
        self.entity_angle = entity_angle
        self.camera_height = camera_height
        self.camera_distance = camera_distance

        self.update()
        

    def get_camera_pos(self):
        camera_x_d = math.sin(math.radians(self.entity_angle)) * self.camera_distance
        camera_z_d = math.cos(math.radians(self.entity_angle)) * self.camera_distance

        camera_x = self.entity.model.pos[0] - camera_x_d
        camera_z = self.entity.model.pos[2] - camera_z_d

        return camera_x, self.camera_height + self.entity.model.pos[1], camera_z

    def get_camera_target_pos(self):
        return self.entity.model.pos

    
    def update(self):
        self.pos = self.get_camera_pos()
        self.target_pos = self.get_camera_target_pos()
    
    @property
    def matrix4(self):
        self.update()
        self._set_camera_matrix()

        return super().matrix4