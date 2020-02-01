from .camera import Camera


class ViewUpCamera(Camera):
    def __init__(self, entity, zoom = 0.1):
        posx, posy, posz = entity.model.pos
        posy += zoom
        super().__init__([0.99, 0.1, 1.2], [1, 0, 1], [0, 1, 0])