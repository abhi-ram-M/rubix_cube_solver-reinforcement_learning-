import pyray as pr
import numpy as np

def handle_cube_keypress(rotation_queue):
    # Right face (R, R')
    if pr.is_key_pressed(pr.KEY_R):
        rotation_queue.append((-np.pi/2, np.array([1, 0, 0]), 2))   # R
    if pr.is_key_pressed(pr.KEY_T):  # alternate for R'
        rotation_queue.append((+np.pi/2, np.array([1, 0, 0]), 2))   # R'

    # Left face (L, L')
    if pr.is_key_pressed(pr.KEY_L):
        rotation_queue.append((-np.pi/2, np.array([1, 0, 0]), 0))   # L
    if pr.is_key_pressed(pr.KEY_K):  # alternate for L'
        rotation_queue.append((+np.pi/2, np.array([1, 0, 0]), 0))   # L'

    # Up face (U, U')
    if pr.is_key_pressed(pr.KEY_U):
        rotation_queue.append((-np.pi/2, np.array([0, 1, 0]), 2))   # U
    if pr.is_key_pressed(pr.KEY_Y):  # alternate for U'
        rotation_queue.append((+np.pi/2, np.array([0, 1, 0]), 2))   # U'

    # Down face (D, D')
    if pr.is_key_pressed(pr.KEY_D):
        rotation_queue.append((-np.pi/2, np.array([0, 1, 0]), 0))   # D
    if pr.is_key_pressed(pr.KEY_M):  # alternate for D'
        rotation_queue.append((+np.pi/2, np.array([0, 1, 0]), 0))   # D'

    # Front face (F, F')
    if pr.is_key_pressed(pr.KEY_F):
        rotation_queue.append((-np.pi/2, np.array([0, 0, 1]), 2))   # F
    if pr.is_key_pressed(pr.KEY_G):  # alternate for F'
        rotation_queue.append((+np.pi/2, np.array([0, 0, 1]), 2))   # F'

    # Back face (B, B')
    if pr.is_key_pressed(pr.KEY_B):
        rotation_queue.append((-np.pi/2, np.array([0, 0, 1]), 0))   # B
    if pr.is_key_pressed(pr.KEY_V):  # alternate for B'
        rotation_queue.append((+np.pi/2, np.array([0, 0, 1]), 0))   # B'

    return rotation_queue
