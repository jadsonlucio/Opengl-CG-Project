from window import Window


class DrawTool(Window):
    def __init__(self, title, width, height, img_width, img_heigh):
        super().__init__(title, width, height)
        
        self.img_buffer = []
        self.type_buffer = []


    def render(self):
        pass