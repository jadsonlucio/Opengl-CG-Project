import numpy as np
from PIL import Image


def read_image(image_path, width, height):
    img = Image.open(image_path)
    resized_img = img.resize((width, width))
    resized_img = resized_img.convert('RGB')
    resized_img_array = np.array(resized_img)

    return resized_img_array


def color_similarity(color_1, color_2, method = "square"):
    """
    Color similarity between two colors.
    """
    def CIE76DeltaE2(color_1,color_2):
        """Returns the square of the CIE76 Delta-E colour distance between 2 lab colours"""
        try:
            if (isinstance(color_1, int) or isinstance(color_1, np.uint8)) and (isinstance(color_2, int) or isinstance(color_2, np.uint8)):
                similarity = (color_1 - color_2)**2
            elif len(color_1) == len(color_2) and len(color_1) == 3:
                similarity = sum((np.array(color_1) - np.array(color_2))**2)
            else:
                raise Exception("Colors must have the same format")

            return similarity
        except Exception as e:
            print(color_1, color_2)
            print(type(color_2), type(color_1))
            raise e

    if method == "square":
        return CIE76DeltaE2(color_1, color_2)
    elif method == "manhattan":
        color_1 = rgb2ind(color_1)
        color_2 = rgb2ind(color_2)

        return abs(color_1 - color_2)

def most_similar_color(color, colors):
    similarity_array = list(map(lambda c: color_similarity(c, color), colors))
    index_min = np.argmin(similarity_array)

    return colors[index_min], similarity_array[index_min]


def change_color_palette(array, color_palette_dict, reverse = False):
    if reverse:
        color_palette_dict = {value : key for key, value in color_palette_dict.items()}

    new_array = []
    for i in range(len(array)):
        row = []
        for j in range(len(array[i])):
            row.append(most_similar_color(array[i][j], color_palette_dict))
        new_array.append(row)
    
    return new_array

