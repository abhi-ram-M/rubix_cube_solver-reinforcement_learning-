import pyray as pr
window_w, window_h = 600, 450
fps = 60

camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

camera.projection = pr.CAMERA_PERSPECTIVE