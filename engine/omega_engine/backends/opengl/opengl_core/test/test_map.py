import noise

from core import *
from pygame_window import Window
from raw import noise_map, get_cube, draw_image_map_v2, draw_image_map

class MapSceen(Window):
    def __init__(self, title, width, height):
        super().__init__(title, 800, 600)
        vertices, vertex_format, indices = draw_image_map_v2("resources/images/test_2.png", 100, 100, 99)
        matrix_model = MatrixModel()
        #self.map_obj = Entity(vertices, vertex_format, indices, None, matrix_model)
        self.map_obj = Entity(vertices, vertex_format, indices, None, matrix_model)
        self.map_obj.model.rotate(25, 1, 0, 0)

        vertices, vertex_format, indices = get_cube()
        cube_texture = Texture.load_texture("resources/textures/sun.png")
        self.light = Light((2,2,0), (1,1,1))
        self.cube_obj = Entity(vertices, vertex_format, indices, cube_texture, None)
        self.cube_obj.model.pos = self.light.pos
        self.cube_obj.model.scale(0.5,0.5,0.5)

        #self.ship = 

        program = Program.load_program("resources/shaders/test_map.shader")
        program.compile()

        program_l = Program.load_program("resources/shaders/test_map_l.shader")
        program_l.compile()

        camera = Camera([0, 0, 1], [0, 0, 0], [0, 1, 0])
        self.projection = Projection(45, 800, 600, 0.1, 100)

        
        self.renderer = Renderer(program, camera, self.projection, self.light)
        self.renderer_1 = Renderer(program_l, camera, self.projection, None)

        self.clock = pygame.time.Clock()
        self.rotate, self.move = False, False
        self.rx, self.ry = False, False
        self.tx, self.ty = 0, 0
        self.zpos = 5
    

    def render(self):
        self.clock.tick(60)
        self.update_camera()
        self.cube_obj.model.rotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.renderer.draw(self.map_obj)
        self.renderer_1.draw(self.cube_obj)

    def on_key_press(self, event):
        if event.key == 273:
            self.move_light(0, 0, 0.1)
        elif event.key == 274:
            self.move_light(0, 0, -0.1)
        elif event.key == 276:
            self.move_light(0.1, 0, 0)
        elif event.key == 275:
            self.move_light(-0.1, 0, 0)
        elif event.key == 280:
            self.move_light(0, 0.1, 0)
        elif event.key == 281:
            self.move_light(0, -0.1, 0)


    def on_mouse_up(self, event):
        if event.button == 1: self.rotate = False
        elif event.button == 3: self.move = False
    
    def on_mouse_down(self, event):
        if event.button == 4: self.zpos = max(1, self.zpos-1)
        elif event.button == 5: self.zpos += 1
        elif event.button == 1: self.rotate = True
        elif event.button == 3: self.move = True


    def on_mouse_motion(self, event):
        i, j = event.rel
        if self.rotate:
            self.rx += i/100
            self.ry += j/100
        if self.move:
            self.tx += i
            self.ty -= j

    def on_resize(self, event):
        self.projection.update(width=event.w, height=event.h)

def main():
    map_screen = MapSceen("teste", 800, 600)
    map_screen.execute()

def test():
    main()


