import pyray as pr
from rubik import Rubik
# from cube_keybindings import handle_cube_keypress
import configs
import numpy as np
from utils import generate_random_moments

pr.init_window(configs.window_w, configs.window_h, "Rubik's Cube")
camera = pr.Camera3D(
    [0.0, 0.0, 20.0],
    [0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    45.0, 0      
)
camera.projection = pr.CAMERA_PERSPECTIVE

rubik_cube = Rubik()
rotation_queue = generate_random_moments(5)


pr.set_target_fps(configs.fps)

while not pr.window_should_close():

    rotation_queue, animation_step = rubik_cube.handle_rotation(rotation_queue)

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.begin_mode_3d(configs.camera)
    pr.draw_grid(20, 1.0)
    for i, cube in enumerate(rubik_cube.cubes):
        for cube_part in cube:
            position = pr.Vector3(cube[0].center[0],cube[0].center[1],cube[0].center[2])
            print(cube[0].center)
            pr.draw_model(cube_part.model,
                          position,
                          2,
                          cube_part.face_color)
    pr.end_mode_3d()
    pr.end_drawing()
pr.close_window()


