# vertex shader
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;
layout (location = 2) in vec3 aNormal;


out vec3 Normal;
out vec3 color;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    vec3 FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    //
    color = aColor;  
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}


# fragment shader
#version 330 core
out vec4 FragColor;

in vec3 Normal;  
in vec3 color;

void main()
{
    FragColor = vec4(color, 1.0);
} 



