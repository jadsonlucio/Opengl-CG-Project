from ...transformation.view import View

class Camera(View):
    def __init__(self, pos, target_pos = (0,0,0), camera_up = (0, 1, 0)):
        super().__init__(pos, target_pos, camera_up)
        