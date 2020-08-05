import sys
from map_generation.draw_map import draw_image_map_v2

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        from game_window import GameWindow
        img_name = args[1]
        game = GameWindow("teste", 1600, 900, img_name)
        game.on_execute()
    elif len(args) == 3:
        img_path = args[1]
        if args[2] == "obj":
            vertices, vertex_format, indices = draw_image_map_v2(img_path, 100, 100, 99)
            
        else:
            raise Exception(f"map can't be exported to the type {sys[2]}")