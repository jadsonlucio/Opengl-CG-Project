import numpy as np

from .image import read_image, most_similar_color, color_similarity
from .map import get_map

colors= [(121, 183, 220),
        (171, 201, 175), 
        (238, 240, 191), 
        (213, 215, 214), 
        (218, 199, 189)] 

color_heights_dict = {
  (121, 183, 220) : -0.05,
  (171, 201, 175) : 0,
  (238, 240, 191) : 0.0,
  (213, 215, 214) : 0.05,
  (218, 199, 189) : 0.025
}

def get_terrain_height_from_draw(img, x, y):
    color = most_similar_color(img[x][y], colors)[0]
    return color_heights_dict[color]

def get_terrain_height_from_draw_v2(img, x, y):
    similaritys = []
    for c in colors:
        similarity = color_similarity(c, img[x][y])
        if similarity == 0:
            similarity = 1
        similaritys.append(1/similarity)

    inverse_sum = sum(similaritys)

    height = sum([(similarity/inverse_sum) * color_heights_dict[c]  
                for c, similarity in zip(colors, similaritys)])

    #print(color)
    return height

def get_terrain_color_from_draw(img, x, y):
    return img[x][y]/255
    

def draw_image_z_color_func(img, width, height, z_func, color_func):
    if isinstance(img, str):
        img = read_image(img, width, height)

    def wrapper(x, y):
        z = z_func(img, x, y)
        color = color_func(img, x, y)
        return z, color

    return wrapper

def draw_image_map(img_path, width, height, normalizantion):
    z_color_func = draw_image_z_color_func(img_path, width, height, 
        get_terrain_height_from_draw, get_terrain_color_from_draw)
    return get_map(width, height, normalizantion, z_color_func)

def draw_image_map_v2(img_path, width, height, normalizantion):
    z_color_func = draw_image_z_color_func(img_path, width, height, 
    get_terrain_height_from_draw_v2, get_terrain_color_from_draw)

    return get_map(width, height, normalizantion, z_color_func)