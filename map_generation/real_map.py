from .image import read_image

def draw_image_z_color_func(img, width, height):
    if isinstance(img, str):
        img = read_image(img)

    def wrapper(x, y):
        return 1, [1,1,1]

    return wrapper