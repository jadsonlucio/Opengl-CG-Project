from core import *
from pygame_window import Window
from raw import get_normal_cube


class LightTest(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        program_object = Program.load_program("resources/shaders/test_light.shader")
        program_object.compile()

        program_light = Program.load_program("resources/shaders/test_light_l.shader")
        program_light.compile()

        camera = Camera([0, 0, 5], [0, 0, 0], [0, 1, 0])
        projection = Projection(45, 800, 600, 0.1, 100)

        self.light = Light((0,0,0), (1,1,1))
        self.renderer_objects = Renderer(program_object, camera, projection, self.light)
        self.renderer_light = Renderer(program_light, camera, projection)

        texture_cube = Texture.load_texture("resources/textures/yep.png")

        vertices, vertex_format, indices = get_normal_cube()
        matrix_model = MatrixModel()
        self.cube = Entity(vertices, vertex_format, indices, texture_cube, matrix_model)
        self.cube.model.scale(2,2,2)
        self.cube_light = self.cube.__copy__()
        self.cube_light.model.scale(0.5,0.5,0.5)
        self.cube_light.model.translate(5, 0, -1)
        self.cube.model.translate(0,0,-1)

        self.angle = 0

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #self.cube.model.rotate(45/1000, 1, 0, 1)
        radius = 3
        self.angle = (self.angle % 360) + 0.01
        pos_x, pos_z = math.sin(math.radians(self.angle)) * radius, math.cos(math.radians(self.angle)) * radius
        self.cube_light.model.pos = [pos_x, 0, pos_z]
        self.light.pos = [pos_x, 0, pos_z]

        #self.renderer_objects.program.set_uniform_vec3f_by_name(np.array([pos_x, 0, pos_z], dtype="float32"), "lightPos", 1)
        #self.renderer_objects.program.set_uniform_vec3f_by_name(np.array(glm.vec3(1, 1.0, 1.0)), "lightColor", 1)
        self.renderer_objects.program.set_uniform_vec3f_by_name(np.array(glm.vec3(1.0, 0.5, 0.31)), "objectColor", 1)
        self.renderer_objects.draw(self.cube)
        self.renderer_light.draw(self.cube_light)


def main():
    window = LightTest("test light", 800, 600)
    window.execute()

def test():
    main()