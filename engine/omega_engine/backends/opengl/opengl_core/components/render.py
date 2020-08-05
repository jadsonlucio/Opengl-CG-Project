from OpenGL.GL import *


class Renderer():
    def __init__(self, program, camera, projection, light=None):
        self.program = program
        self.camera = camera
        self.projection = projection
        self.light = light
        self._setup()

    def _setup(self):
        glClearColor(0, 0, 0.2, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def draw(self, *entitys):
        self.program.use()
        self.program.set_uniform_matrix4f_by_name(self.camera.matrix4, "view", 1)
        self.program.set_uniform_matrix4f_by_name(self.projection.matrix4, "projection", 1)

        if self.light != None:
            self.program.set_uniform_vec3f_by_name(self.light.pos, "lightPos", 1)
            self.program.set_uniform_vec3f_by_name(self.light.color, "lightColor", 1)

        for entity in entitys:
            entity.draw(self.program)
