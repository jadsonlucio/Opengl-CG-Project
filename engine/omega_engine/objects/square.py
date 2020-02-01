import numpy as np
from OpenGL.GL import GL_FLOAT

vertices = [-0.5, -0.5, 0, 1.0, 1.0, 1.0, 0.0,  0.0, -1.0,
            0.5, -0.5, 0,  1.0, 1.0, 1.0, 0.0,  0.0, -1.0, 
            0.5,  0.5, 0,  1.0, 1.0, 1.0, 0.0,  0.0, -1.0, 
            -0.5, -0.5, 0,  1.0, 1.0, 1.0, 0.0,  0.0, -1.0, 
            0.5,  0.5, 0, 1.0, 1.0, 1.0, 0.0,  0.0, -1.0, 
            -0.5, 0.5, 0, 1.0, 1.0, 1.0, 0.0,  0.0, -1.0]

indices = [
    0, 1, 2, 3, 4, 5
]

vertices = np.array(vertices, dtype=np.float32)
indices = np.array(indices, dtype=np.uint32)

vertex_format =  [[3, GL_FLOAT, 0], [3, GL_FLOAT, 1], [3, GL_FLOAT, 2]]

def get_square():
    return vertices, vertex_format, indices