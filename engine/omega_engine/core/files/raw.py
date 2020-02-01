import numpy as np
from ..graphics.material import Material

def load_materials_file(file_path):
    file = open(file_path, "r")
    materials = {}
    curr_material = {}

    material_attrs = {"Ns" : "ns",
                      "Ka" : "ka",
                      "Kd" : "kd",
                      "Ks" : "ks",
                      "Ni" : "ni",
                      "d"  : "d",
                      "illum" : "illum"}

    start_with_attr = lambda string: any([string.startswith(attr) for attr in material_attrs])

    for line in file.readlines():
        if line.startswith("newmtl"):
            if len(curr_material) != 0:
                material = Material(**curr_material)
                materials[material.name] = material
                curr_material = {}

            material_name = line.split(" ")[-1].replace("\n", "")
            curr_material["name"] = material_name

        elif start_with_attr(line):
            attr = line.split(" ")
            attr_name, attr_value = attr[0], attr[1:]
            attr_name = material_attrs[attr_name]

            if len(attr_value) == 1:
                attr_value = float(attr_value[0])
            else:
                attr_value = [float(c) for c in attr_value]

            curr_material[attr_name] = attr_value
    
    material = Material(**curr_material)
    materials[material.name] = material

    return materials

def duplicate_data(data, indices, duplicate_data):
    for i in range(1, len(indices) - 1):
        duplicate_data += [data[indices[0] - 1], data[indices[i] - 1], data[indices[i+1] - 1]]
    

def load_obj_data(file_obj_path, file_materials_path = None):
    materials = {}
    if file_materials_path != None:
        materials = load_materials_file(file_materials_path)
    
    print(file_obj_path)
    print(file_materials_path)
    file = open(file_obj_path, "r")

    vertices_data = []
    normals_data = []
    colors_data = []
    textures_data = []

    vertices = []
    normals = []
    textures = []
    colors = []
    indices = []

    curr_material = None

    for line in file.readlines():
        line = line.replace("\n", "")
        if line.startswith("#") : continue
        elif line == "" : continue
        else:
            elements = line.split(" ")
            elements = [e for e in elements if e != "" and e != " "]
            if elements[0] == "usemtl":
                curr_material = elements[1]
            if elements[0] == "v":
                vertices_data.append([float(v) for v in elements[1:]])
            elif elements[0] == "vn":
                normals_data.append([float(n) for n in elements[1:]])
            elif elements[0] == "vt":
                textures_data.append([float(n) for n in elements[1:]])
            elif elements[0] == "f":
                indices_vertices = []
                indices_normals = []
                indices_colors = []
                indices_textures = []

                if "//" in elements[1]:
                    for e in elements[1:]:
                        v = [int(a) for a in e.split("//")]
                        if len(v) == 1:
                            indices_vertices.append(v[0])
                        elif len(v) == 2:
                            indices_vertices.append(v[0])
                            indices_normals.append(v[1])
                        elif len(v) == 3:
                            indices_vertices.append(v[0])
                            indices_normals.append(v[1])
                            indices_colors.append(v[2])
                elif "/" in elements[1]:
                    for e in elements[1:]:
                        v = [int(a) for a in e.split("/")]
                        if len(v) == 1:
                            indices_vertices.append(v[0])
                        elif len(v) == 2:
                            indices_vertices.append(v[0])
                            indices_textures.append(v[1])
                        elif len(v) == 3:
                            indices_vertices.append(v[0])
                            indices_textures.append(v[1])
                            indices_normals.append(v[2])
                else:
                    for e in elements[1:]:
                        indices_vertices.append(int(e))

                duplicate_data(vertices_data, indices_vertices, vertices)
                duplicate_data(normals_data, indices_normals, normals)
                duplicate_data(colors_data, indices_colors, colors)
                duplicate_data(textures_data, indices_textures, textures)

                if len(indices_colors) == 0 and curr_material != None:
                    for c in range(0,3 * (len(indices_vertices) - 2)):
                        colors.append(materials[curr_material].kd)
                
    indices = [*range(0, len(vertices))]

    return vertices, normals, colors, indices



if __name__ == "__main__":
    mrl_file_path = "D:/dev/Programação/Github/Faculdade/Atividades disciplinas/6 periodo/CG/pyopengl tutorial/humvee.mtl"
    obj_file_path = "D:/dev/Programação/Github/Faculdade/Atividades disciplinas/6 periodo/CG/pyopengl tutorial/humvee.obj"
    vertices, normals, colors, indices = load_obj_data(obj_file_path, mrl_file_path)
    print(len(vertices))
    print(len(normals))
    print(len(colors))


