import noise
from .map import get_map

def get_terrain_height_from_noise(x, y):
    shape = (1024,1024)
    scale = 100.0
    octaves = 100
    persistence = 0.5
    lacunarity = 2.0

    return noise.pnoise2(x/scale, 
                        y/scale, 
                        octaves=octaves, 
                        persistence=persistence, 
                        lacunarity=lacunarity, 
                        repeatx=1024, 
                        repeaty=1024, 
                        base=0)

def get_terrain_color(z):
    if z < -0.05:
        return [0.19607843, 0.62352941, 0.89019608]
    elif z < 0.0:
        return [0.19607843, 0.89019608, 0.34509804]
    else:
        return [0.68627451, 0.68627451, 0.68627451]


def noise_z_color_func():
    def wrapper(x, y):
        z = get_terrain_height_from_noise(x, y)
        color = get_terrain_color(z)

        return z, color

    return wrapper

def noise_map(map_sizex, map_sizey, normalizantion):
    z_color_func = noise_z_color_func()
    return get_map(map_sizex, map_sizey, normalizantion, z_color_func)