import ctypes
import numpy as np
from OpenGL.GL import *

from ..raw import load_obj_data
from ..transformation.model import MatrixModel

class Entity():
    def __init__(self, vertices, vertex_format, indices, texture = None, model = None):
        self.vertices = vertices
        self.vertex_format = np.array(vertex_format)
        self.indices = indices
        self.texture = texture
        if model == None:
            model = MatrixModel()
        self.model = model

        self.vao = glGenVertexArrays(1)
        self.vbo = None
        self.ibo = None

        self.gen_vertex_buffer()
        self.populate_vao()

    def gen_vertex_buffer(self):
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        self.ibo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ibo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)


    def populate_vao(self):
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        stride = self.vertex_format.transpose()[0].sum() * 4
        pointer_v = 0

        for size, dtype, position in self.vertex_format:
            glEnableVertexAttribArray(position)
            glVertexAttribPointer(position, size, dtype, False, stride, ctypes.c_void_p(int(pointer_v)))
            pointer_v += size * 4

    
    def draw(self, program):
        if self.texture:
            self.texture.bind()
        program.use()
        program.set_uniform_matrix4f_by_name(self.model.matrix4, "model", 1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ibo)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

    def __copy__(self):
        entity = Entity.__new__(Entity)
        entity.vertices = self.vertices
        entity.indices = self.indices
        entity.vertex_format = self.vertex_format
        entity.texture = self.texture
        entity.model = MatrixModel()
        entity.vao = self.vao
        entity.vbo = self.vbo
        entity.ibo = self.ibo
        

        return entity

    @classmethod
    def load_obj(cls, obj_file_path, mtl_file_path):
        vertices, normals, colors, indices = load_obj_data(obj_file_path, mtl_file_path)

        _vertices_data = []
        print(np.array(vertices).shape)
        print(np.array(normals).shape)
        print(np.array(colors).shape)
        
        for vertice, normal, color in zip(vertices, normals, colors):
            _vertices_data += vertice + color + normal

        vertex_format = [[3, GL_FLOAT, 0], [3, GL_FLOAT, 1], [3, GL_FLOAT, 2]]

        _vertices_data = np.array(_vertices_data, dtype="float32")
        indices = np.array(indices, dtype="uint32")
        return Entity(_vertices_data, vertex_format, indices)

        




