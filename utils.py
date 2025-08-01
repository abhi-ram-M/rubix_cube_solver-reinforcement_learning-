import configs
import numpy as np

def generate_random_moments(n):
    rotation_queue = []

    for _ in range(n):
        action = np.random.choice(list(configs.rubiks_moves.keys()))
        rotation_queue.append(configs.rubiks_moves[action])
    return rotation_queue
