import sys
from map_generation.draw_map import draw_image_map_v2

if __name__ == "__main__":
    if len(sys) == 2:
        from game_window import GameWindow
        img_name = sys[1]
        game = GameWindow("teste", 800, 600, img_name)
        game.on_execute()
    elif len(sys) == 3:
        img_path = sys[1]
        if sys[2] == "obj":
            vertices, vertex_format, indices = draw_image_map_v2(img_path, 100, 100, 99)
            
        else:
            raise Exception(f"map can't be exported to the type {sys[2]}")