# vertex shader
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 2) in vec2 aTexPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;


out vec2 v_texPos;

void main()
{
	gl_Position = projection * view * model * vec4(aPos, 1.0);
    v_texPos = aTexPos;
}

# fragment shader
#version 330 core

in vec2 v_texPos;
out vec4 FragColor;

uniform sampler2D s_texture;

void main()
{
    FragColor = texture(s_texture, v_texPos); // set alle 4 vector values to 1.0
}


