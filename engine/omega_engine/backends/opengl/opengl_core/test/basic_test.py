from core import *
from pygame_window import Window

from raw import get_cube

class BasicTest(Window):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        
        program = Program.load_program("resources/shaders/basic_test.shader")
        program.compile()
    
        texture_cube = Texture.load_texture("resources/textures/yep.png")

        camera = Camera([0, 0, 5], [0, 0, 0], [0, 1, 0])
        projection = Projection(45, 800, 600, 0.1, 100)

        self.renderer = Renderer(program, camera, projection)

        vertices, vertex_format, indices = get_cube()
        matrix_model = MatrixModel()
        self.cube = Entity(vertices, vertex_format, indices, texture_cube, matrix_model)
        self.cube2 = self.cube.__copy__()
        self.cube2.model.translate(2, 0 , -5)
        
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cube.model.rotate(45/1000, 1, 0, 1)
        self.renderer.draw(self.cube, self.cube2)



def main():
    window = BasicTest("basic test", 800, 600)
    window.execute()

def test():
    main()

if __name__ == "__main__":
    main()