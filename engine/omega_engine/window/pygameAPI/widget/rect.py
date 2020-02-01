import numpy as np

class Rect:
    def __init__(self, master_rect, relposX, relposY, width, height):
        self.master_rect = master_rect
        self.relposX = relposX
        self.relposY = relposY
        self.width = width
        self.height = height
    
    
    def relpos(self):
        return np.array([self.relposX, self.relposY])

    def abspos(self):
        if isinstance(master_rect, Rect):
            return np.array([self.master_rect.abspos + self.relpos])
        else:
            return self.relpos