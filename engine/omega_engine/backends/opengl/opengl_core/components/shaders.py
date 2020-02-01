from OpenGL.GL import *

class Program():
    current_program = None

    def __init__(self, vertex_src, fragment_src, file_path):
        self.file_path = file_path
        self.vertex_shader = Shader(vertex_src, GL_VERTEX_SHADER)
        self.fragment_shader = Shader(fragment_src, GL_FRAGMENT_SHADER)
        self.obj = None

    def compile(self):
        self.vertex_shader.compile()
        self.fragment_shader.compile()
        self.obj = glCreateProgram()
        glAttachShader(self.obj, self.vertex_shader.obj)
        glAttachShader(self.obj, self.fragment_shader.obj)

        glLinkProgram(self.obj)

        return self.obj

    def use(self):
        if Program.current_program != self.obj:
            glUseProgram(self.obj)
            Program.current_program = self.obj

    def get_uniform_location(self, name):
        return glGetUniformLocation(self.obj, name)

    def set_uniform_matrix4f(self, matrix, uniform_loc, num_matrix, transpose = GL_FALSE):
        self.use()
        glUniformMatrix4fv(uniform_loc, num_matrix, transpose, matrix)

    def set_uniform_vec3f(self, vec3, uniform_loc, num_vec3):
        self.use()
        glUniform3fv(uniform_loc, num_vec3, vec3)

    def set_uniform_matrix4f_by_name(self, matrix, uniform_name, num_matrix, transpose = GL_FALSE):
        uniform_loc = self.get_uniform_location(uniform_name)
        self.set_uniform_matrix4f(matrix, uniform_loc, num_matrix, transpose)

    def set_uniform_vec3f_by_name(self, vec3, uniform_name, num_vec3):
        uniform_loc = self.get_uniform_location(uniform_name)
        self.set_uniform_vec3f(vec3, uniform_loc, num_vec3)

    @classmethod
    def load_program(cls, file_path):
        arq = open(file_path, "r")
        shaders_src = {
            "fragment_src": "",
            "vertex_src": "",
        }
        shader_src_type = None
        for line in arq.readlines():
            if "# fragment shader" in line:
                shader_src_type = "fragment_src"
            elif "# vertex shader" in line:
                shader_src_type = "vertex_src"
            elif shader_src_type != None:
                shaders_src[shader_src_type] += line
        
        return Program(**shaders_src, file_path = file_path) 

class Shader():
    def __init__(self, shader_src, shader_type):
        self.src = shader_src
        self.type = shader_type
        self.obj = None

    def compile(self):
        self.obj = glCreateShader(self.type)
        glShaderSource(self.obj, self.src)
        glCompileShader(self.obj)

        self.compile_erros()
    
    def compile_erros(self):
        result = glGetShaderiv(self.obj, GL_COMPILE_STATUS)
        if result == GL_FALSE:
            message  = glGetShaderInfoLog(self.obj)
            raise Exception(f"[Error] {message}")
