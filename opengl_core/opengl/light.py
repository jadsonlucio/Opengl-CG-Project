import numpy as np

class Light():
    def __init__(self, pos, color):
        self._pos = pos 
        self._color = color

    @property
    def pos(self):
        return np.array(self._pos, dtype = "float32")

    @pos.setter
    def pos(self, new_pos):
        self._pos = new_pos

    @property
    def color(self):
        return np.array(self._color, dtype = "float32")

    @color.setter
    def color(self, new_color):
        self._color = new_color

    
    def move(self, x, y, z):
        self._pos = (np.array(self._pos) + np.array([x, y, z])).tolist()