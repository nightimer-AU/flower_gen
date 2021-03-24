
# core_basic_window.py

from raylibpy import *


def main():
    size = 64
    init_window(800, 450, "flower_gen")

    set_target_fps(60)

    while not window_should_close():

        begin_drawing()
        clear_background(RAYWHITE)
        draw_text("###", 190, 200, 20, LIGHTGRAY)
        end_drawing()

    close_window()


if __name__ == '__main__':
    main()