# Opengl-CG-Project

This project aims to create low-poly 3d terrains from images. all the implementation was done in python and the opengl with pyopengl (opengl api to python).

# Getting Started

## Prerequisites

python >= 3.7

## Installing


Fist install virtual environment:

    $ cd translate-app-tkinter
    $ pip install virtualenv 
    $ virtualenv venv

    # on linux
    $ source venv/bin/activate

    # on windows
    $ venv\Scripts\activate.bat

    # now install dependencies
    $ pip -r requirements.txt


# Running 

The following command create an window with the 3d terrain from an image.

    # The image must be in folder resources/images
    $ python main.py image_name

The following command create .obj file of image

    # The image must be in folder resources/images
    $ python main.py image_name obj


# How works

To create the 3d map, an image is passed as an input, as well as the desired size of the map. The map generation process works as follows:

1. First the image is resized to the desired size of the map
2. Then a grid of triangles the size of the map is created according to the figure below, in which each vertex has the position (x, 0, z), that is, the points on the plane have no height.
![img](/assets/images/image7.png)
3. The next step is to calculate the height of each vertex, then for each point of the grid the corresponding pixel in the image is selected and from the following calculation the height of that vertex is determined.
    - A height is previously determined for each color that you want to map as a terrain. The colors, their respective types of terrain and their height are shown in the following table:
    ![img](/assets/images/table_colors.png)
    - Now the height of the vertex at the point (x, y) of the grid is calculated according to the following formula:
    
    ![img](/assets/images/image1.png)
    - This formula aims to assign a weight to the influence of each color on the final height of the vertex, making colors closer to the color of the pixel have a greater influence on the final size of the vertex. At the end of this stage the map should look more or less like the figure below:
    ![img](/assets/images/image13.png)
    - The color of each vertex is the pixel color of the image associated with it. The color of the triangle is the average of the colors of the three pixels associated with it.
    - The vertex normals were calculated using the plane of the triangle associated with this vertex, according to the following formula.
    - And U = p2 - p1 and V = p3 - p1, we have
      Normal (Va, Vb, Vc) = (UyVz - UzVy, UzVx - UxVz, UxVy - UyVx)
    - Once the normals, the color and height of the vertices have been calculated, a process of duplicating vertices must happen, because if a vertex shares more than one triangle, when opengl will treat its color it will end up interleaving the colors this vertex which will cause a texture effect in which the colors of the triangles will be mixed, making the appearance of the low-poly terrain unfeasible.
    - The process of duplicating the vertices consists of for each triangle in the grid taking the vertices associated with it, copying them and adding to a new list of vertices.

## Rendering process structure

First, the vertices, colors, normals and indexes of the map are generated using the method of session 1 from the selected drawing. After that, a buffer is created that joins the data of vertices, colors and normals, which is called the vertex buffer, for indexes and an index buffer is created. As the vertex buffer as the index buffer are associated with a map entity that concentrates the information necessary to draw an object on the screen.

With the map created, the entities necessary to create the render are loaded, which serves as a central point to draw the objects. Entities such as a camera, shaders and projection matrix are loaded in this step. To draw the object, it is necessary to call the render entity's drawing function passing the map entity, in this way the render will perform all the necessary process to draw the map, such as setting the transformation matrices and linking the data of the map's vertices in the shaders . The figure below shows a diagram of the architecture used in modern opengl.

![img](/assets/images/image6.png)

## Results

The images below show the 3d low-polly terrains that were created with this technique:

![title](/assets/images/image10.png)![alt-text-2](/assets/images/image11.png)

![title](/assets/images/image12.png)![alt-text-2](/assets/images/image5.png)

![title](/assets/images/image14.png)![alt-text-2](/assets/images/image17.png)

![title](/assets/images/image9.jpg)![alt-text-2](/assets/images/image15.png)


# Authors

Jadson Lucio dos Santos <br>
Email: jadsonaluno@hotmail.com <br>
Linkedin: https://www.linkedin.com/in/jadson-l-573398b6/

# License

This project is licensed under the MIT License - see the LICENSE.txt file for details