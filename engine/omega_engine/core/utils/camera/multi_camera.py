from .camera import Camera

class MultCamera(Camera):
    def __init__(self, selected, *cameras):
        self.cameras = cameras
        self._selected_cam = self.cameras[selected]
        self._index = selected

        super().__init__(self.selected_cam.pos, self.selected_cam.target_pos,
                                                 self.selected_cam.camera_up)


    @property
    def matrix4(self):
        return self.selected_cam.matrix4

    @property
    def selected_cam(self):
        return self._selected_cam

    @selected_cam.setter
    def selected_cam(self, cam):
        if isinstance(cam, int):
            self._selected_cam = self.cameras[cam]
            self._index = cam
    

    
