# vertex shader
# version 330 core

layout (location = 0) in vec3 a_position;
layout (location = 1) in vec3 a_color;
layout (location = 2) in vec2 a_texture;

uniform mat4 model; // Combined rotation and translation
uniform mat4 projection;
uniform mat4 view;

out vec3 v_color;
out vec2 v_texture;

void main(){
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_color = a_color;
    v_texture = a_texture;

    // v_texture = 1 - a_texture;   // Flips the texture vertically and horizontally
    // v_texture = vec2(a_texture.s, 1 - a_texture.t); // Flips the texture vertically
}


# fragment shader
# version 330 core

in vec3 v_color;
in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main(){
    out_color = texture(s_texture, v_texture);  // vec4(v_color, 1.0);
}



