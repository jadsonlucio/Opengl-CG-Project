from opengl_core import *
from opengl_core.raw import get_normal_cube

class Ship():
    def __init__(self, ):
        vertices, vertex_format, indices = get_normal_cube()
        #Entity(vertices, vertex_format, indices, None, None)
        self.ship_obj = Entity.load_obj("resources/objs/ww 1 for ele.obj", "resources/objs/ww 1 for ele.mtl")
        #self.ship_obj.model.rotate(40, 1, 0, 0)
        self.ship_obj.model.scale(0.0002, 0.0002, 0.0002)
        self.ship_obj.model.pos = (0.5, 0, 0.5)
        self.aceleration = 0.1
        self.speed = 0.1
        self.camera = Camera3RDPerson(self.ship_obj, 0, 0.06, 0.12)
    

    def move(self):
        """x_increase = math.cos(math.radians(self.camera.entity_angle + 90)) * self.speed
        z_increase = math.sin(math.radians(self.camera.entity_angle + 90)) * self.speed"""
        self.ship_obj.model.translate(0, 0, 5)

    def rotate(self, dir):
        self.camera.entity_angle += dir
        self.ship_obj.model.rotate(dir, 0, 1, 0)


    def fly(self, dir):
        self.ship_obj.model.translate(0, dir, 0)

    
    def get_rect_vertices(self):
        pass