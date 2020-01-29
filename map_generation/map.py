import numpy as np
from OpenGL.GL import *

from PIL import Image

def get_normal(p1, p2, p3):
    p1, p2, p3 = np.array(p1), np.array(p2), np.array(p3)
    return np.cross(p2-p1, p3-p1).tolist()

def generate_duplicate_terrain_data(vertices, colors, indices):
    data = []
    new_indices = []
    for v in range(0, len(indices), 3):
        i1, i2, i3 = indices[v], indices[v+1], indices[v+2]
        v1, v2, v3 = list(vertices[i1]), list(vertices[i2]), list(vertices[i3])
        color_v1, color_v2, color_v3 = list(colors[i1]), list(colors[i2]), list(colors[i3]) 
        color = ((np.array(color_v1) + np.array(color_v2) + np.array(color_v3))/3).tolist()
        normal = get_normal(v1, v2, v3)
        data += v1 + color + normal + v2 + color + normal + v3 + color + normal

        new_indices += [v, v+1, v+2]

    return data, new_indices


def generate_terrain_vertices(sizeX, sizeY, normalizantion, z_color_func):
    vertices = []
    colors = []
    indices = []

    for x in range(sizeX):
        for y in range(sizeY):
            z, color = z_color_func(x, y)

            vertices.append([x/normalizantion, z, y/normalizantion])
            colors.append(color)

            if x < (sizeX - 1) and y < (sizeY - 1):
                fist_point = y + x*sizeX
                indices += [fist_point, fist_point+1, fist_point+sizeX]
                indices += [fist_point+1, fist_point+sizeX, fist_point+sizeX+1]
    
    Image.fromarray(np.array(colors, dtype="uint8").reshape(100, 100, 3)).save("image_2.png")
    data, indices = generate_duplicate_terrain_data(vertices, colors, indices)
    return data, indices

def get_map(map_sizex, map_sizey, normalizantion, z_color_func):
    vertices, vertices_indices = generate_terrain_vertices(map_sizex,
                         map_sizey, normalizantion, z_color_func)
    vertices = np.array(vertices, dtype = "float32")
    vertices_indices = np.array(vertices_indices, dtype = "uint32")


    vertex_format = [[3, GL_FLOAT, 0], [3, GL_FLOAT, 1], [3, GL_FLOAT, 2]]

    return vertices, vertex_format, vertices_indices


if __name__ == "__main__":
    get_map(2, 2, 1)