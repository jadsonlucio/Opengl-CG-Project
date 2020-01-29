import pygame
from OpenGL.GL import *

class Texture():
    current_tex = None

    def __init__(self, data, img_width, img_height, internalformat, tex_format, tex_type):
        self.data = data
        self.img_width = img_width
        self.img_height = img_height
        self.internalformat = internalformat
        self.format = tex_format
        self.type = tex_type

        # Textures
        self.obj = glGenTextures(1)
        self.bind()
        glTexImage2D(GL_TEXTURE_2D, 0, internalformat, img_width, 
                    img_height, 0, tex_format, tex_type, data)

    def bind(self):
        if self.current_tex != self.obj:
            glBindTexture(GL_TEXTURE_2D, self.obj)
            
            # Set the texture wrapping parameters
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            # Set the texture filtering parameters
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    @classmethod
    def load_texture(self, file_path):
        image = pygame.image.load(file_path)
        image = pygame.transform.flip(image, False, True)
        img_width, img_height = image.get_rect().size
        img_data = pygame.image.tostring(image, "RGBA")

        return Texture(img_data, img_width, img_height, GL_RGBA, GL_RGBA, GL_UNSIGNED_BYTE)

