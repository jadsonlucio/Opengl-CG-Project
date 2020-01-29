from opengl_core import *
from opengl_core.raw import get_cube
from map_generation.noise_map import noise_map
from map_generation.draw_map import draw_image_map, draw_image_map_v2
from ship import Ship


class Map():
    def __init__(self):
        vertices, vertex_format, indices = draw_image_map_v2("resources/images/test_14.jpeg", 100, 100, 99)
        self.map_obj = Entity(vertices, vertex_format, indices, None, None)
        #self.map_obj.model.rotate(25, 1, 0, 0)
        self.sun = self.load_sun()

        program = Program.load_program("resources/shaders/test_map.shader")
        program.compile()

        program_l = Program.load_program("resources/shaders/test_map_l.shader")
        program_l.compile()
        
        

        self.ship = Ship()
        self.world_camera = Camera([5, 5, -5], [0, 0, 0], [0, 1, 0])
        self.camera = MultCam(1, self.world_camera, self.ship.camera)
        #self.camera = self.ship.camera
        #self.camera = ViewUpCamera(self.ship.ship_obj)
        self.projection = Projection(math.radians(20), 800, 600, 0.1, 100)
        self.renderer = Renderer(program, self.camera, self.projection, self.light)
        self.renderer_1 = Renderer(program_l, self.camera, self.projection, None)

        self.sky = self.load_sky()

        self.clock = pygame.time.Clock()
        self.rotate, self.move = False, False
        self.rx, self.ry = False, False
        self.tx, self.ty = 0, 0
        self.zpos = 5
    
    def load_sun(self):
        vertices, vertex_format, indices = get_cube()
        cube_texture = Texture.load_texture("resources/textures/sun.png")
        self.light = Light((2,2,0), (1,1,1))
        self.cube_obj = Entity(vertices, vertex_format, indices, cube_texture, None)
        self.cube_obj.model.pos = self.light.pos
        self.cube_obj.model.scale(0.5,0.5,0.5)

        return self.cube_obj

    def load_sky(self):
        vertices, vertex_format, indices = get_cube()
        cube_texture = Texture.load_texture("resources/textures/glass2.png")
        cube_obj = Entity(vertices, vertex_format, indices, cube_texture, None)
        cube_obj.model.translate(0.5, 0, 0.5)

        return cube_obj

    def load_player(self):
        pass

    def move_light(self, x, y, z):
        self.light.move(x, y, z)
        self.cube_obj.model.translate(x, y, z)

    def update_camera(self):
        self.world_camera.load_identity()
        self.world_camera.translate(self.tx/40., self.ty/40., - self.zpos)
        self.world_camera.rotate(self.rx, 1, 0, 0)
        self.world_camera.rotate(self.ry, 0, 1, 0)
