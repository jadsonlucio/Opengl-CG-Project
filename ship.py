import glm
from omega_engine.core import *
from omega_engine.backends.opengl import *
from omega_engine.objects import *


class Ship(Particle, Entity):
    def __init__(self):
        vertices, vertex_format, indices = Entity.load_obj("resources/objs/ww 1 for ele.obj",
                                                           "resources/objs/ww 1 for ele.mtl")
        Particle.__init__(self, 1, 1, 1, 1, 1, 1, 1)
        Entity.__init__(self, vertices, vertex_format, indices)

        # self.ship_obj.model.rotate(40, 1, 0, 0)
        self.model.scale(0.0002, 0.0002, 0.0002)
        self.model.pos = (-0.25, 0, -0.25)
        self.aceleration = 0.1
        self.speed = 0.1
        self.camera = CameraAirPlane(self, 250, 500)

    def move(self):
        # x_increase = math.cos(math.radians(self.camera.x_angle + 90)) * self.speed
        # z_increase = math.sin(math.radians(self.camera.x_angle + 90)) * self.speed
        pre_pos = glm.vec3(glm.column(glm.translate(glm.mat4(self.model.matrix4), glm.vec3(0, 0, 5)), 3))
        if pre_pos[0] <= 0.49 and pre_pos[0] >= -0.49 \
                and pre_pos[1] <= 0.49 and pre_pos[1] >= 0 \
                and pre_pos[2] <= 0.49 and pre_pos[2] >= -0.49:
            self.model.translate(0, 0, 5)

    def rotate(self, x_angle=0, y_angle=0, z_angle=0):
        self.model.rotate(x_angle, 1, 0, 0)
        self.model.rotate(y_angle, 0, 1, 0)
        self.model.rotate(z_angle, 0, 0, 1)
        self.camera.rotate(x_angle=x_angle)
        self.camera.rotate(y_angle=y_angle)
        self.camera.rotate(z_angle=z_angle)

    def fly(self, dir):
        self.model.translate(0, dir, 0)

    def get_rect_vertices(self):
        pass
