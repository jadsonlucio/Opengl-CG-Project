from core import *
from pygame_window import Window

from raw import get_cube, get_square

class BasicTest(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        
        program = Program.load_program("test/resources/shaders/test_load_obj.shader")
        program.compile()
    
        camera = Camera([0, 0, 5], [0, 0, 0], [0, 1, 0])
        projection = Projection(45, 800, 600, 0.1, 100)

        self.renderer = Renderer(program, camera, projection)

        texture_cube = Texture.load_texture("test/resources/textures/yep.png")
        self.obj = Entity.load_obj("test/resources/objs/humvee.obj", "test/resources/objs/humvee.mtl")
        print(self.obj.vertices)

        vertices, vertex_format, indices = get_cube()
        self.cube = Entity(vertices, vertex_format, indices, texture_cube)

        vertices, vertex_format, indices = get_square()
        self.square = Entity(vertices, vertex_format, indices)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.obj.model.rotate(0.1, 0, 1, 0)
        self.renderer.draw(self.obj)



def main():
    window = BasicTest("basic test", 800, 600)
    window.execute()

def test():
    main()

if __name__ == "__main__":
    main()