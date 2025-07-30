import pyray as pr
import numpy as np

class Cube:
    def __init__(self, size, center, face_color):
        self.size = size
        self.center = center
        self.face_color = face_color
        self.orientation = np.eye(3)

        self.model = None
        self.gen_meshe(size)
        self.create_model()

    def gen_meshe(self, scale: tuple):
        self.mesh = pr.gen_mesh_cube(*scale)

    def create_model(self):
        self.model = pr.load_model_from_mesh(self.mesh)
        self.model.transform = pr.matrix_translate(self.center[0], self.center[1], self.center[2])

class Rubik:
    def __init__(self) -> None:
        self.cubes = []
        self.generate_rubik(2)
    
    def generate_rubik(self, size):
        colors = [pr.RED, pr.ORANGE, pr.GREEN, pr.BLUE, pr.WHITE, pr.YELLOW]
        offset = size - 0.7
        size_x = (size*0.9, size*0.1, size*0.9)
        size_y = (size*0.1, size*0.9, size*0.9)
        size_z = (size*0.9, size*0.9, size*0.1)
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    # Face color assignment by position:
                    face_colors = [
                        colors[0] if z == 2 else pr.BLACK,
                        colors[1] if z == 0 else pr.BLACK,
                        colors[2] if x == 2 else pr.BLACK,
                        colors[3] if x == 0 else pr.BLACK,
                        colors[4] if y == 2 else pr.BLACK,
                        colors[5] if y == 0 else pr.BLACK 
                    ]
                    center_position = np.array([(x - 1)*offset, 
                                               (y - 1)*offset,
                                               (z - 1)*offset])
                    center = Cube((size, size, size), center_position, pr.BLACK)

                    front_position = np.array([center_position[0],
                                               center_position[1],
                                               center_position[2] + size/2])
                    front = Cube(size_z, front_position, face_colors[0])

                    back_position = np.array([center_position[0],
                                              center_position[1],
                                              center_position[2] - size/2])
                    back = Cube(size_z, back_position, face_colors[1])

                    right_position = np.array([center_position[0] + size/2,
                                               center_position[1],
                                               center_position[2]])
                    right = Cube(size_y, right_position, face_colors[2])

                    left_position = np.array([center_position[0] - size/2,
                                              center_position[1],
                                              center_position[2]])
                    left = Cube(size_y, left_position, face_colors[3])

                    top_position = np.array([center_position[0],
                                             center_position[1] + size/2,
                                             center_position[2]])
                    top = Cube(size_x, top_position, face_colors[4])

                    bottom_position = np.array([center_position[0],
                                                center_position[1] - size/2,
                                                center_position[2]])
                    bottom = Cube(size_x, bottom_position, face_colors[5])
                    
                    self.cubes.append([center, front, back, right, left, top, bottom])
        return self.cubes



# import pyray as pr
# import numpy as np

# class Cube:
#     def __init__(self, size, center, face_color):
#         self.size = size
#         self.center = center
#         self.face_color = face_color
#         self.orientation = np.eye(3)

#         self.model = None
#         self.gen_meshe(size)
#         self.create_model()

#     def gen_meshe(self, scale: tuple):
#         self.mesh = pr.gen_mesh_cube(*scale)

#     def create_model(self):
#         self.model = pr.load_model_from_mesh(self.mesh)
#         self.model.transform = pr.matrix_translate(self.center[0], self.center[1], self.center[2])

# class Rubik:
#     def __init__(self) -> None:
#         self.cubes = []
#         self.generate_rubik(2)
    
#     def generate_rubik(self, size):
#         colors = [pr.WHITE, pr.BLUE, pr.ORANGE, pr.RED, pr.YELLOW, pr.GREEN]
#         offset = size-0.7
#         size_x = size*0.9, size*0.9, size*0.1
#         size_y = size*0.9, size*0.1, size*0.9
#         size_z = size*0.1, size*0.9, size*0.9
#         for x in range(3):
#             for y in range(3):
#                 for z in range(3):
#                     face_colors = [
#                         pr.BLACK if z != 2 else colors[0],
#                         pr.BLACK if z != 0 else colors[1],
#                         pr.BLACK if x != 2 else colors[2],
#                         pr.BLACK if x != 0 else colors[3],
#                         pr.BLACK if y != 2 else colors[4],
#                         pr.BLACK if y != 0 else colors[5]
#                     ]
#                     center_position = np.array([(x -1)*offset, 
#                                                (y-1)*offset,
#                                                (z-1)*offset])
#                     center = Cube((size, size, size), center_position, pr.BLACK)

#                     front_position = np.array([center_position[0],
#                                                center_position[1],
#                                                center_position[2] - size/2])
#                     front = Cube(size_z, front_position, face_colors[0])

#                     back_position = np.array([center_position[0],
#                                               center_position[1],
#                                               center_position[2] + size/2])
#                     back = Cube(size_z, back_position, face_colors[1])

#                     right_position = np.array([center_position[0] + size/2,
#                                                center_position[1],
#                                                center_position[2]])
#                     right = Cube(size_y, right_position, face_colors[2])

#                     left_position = np.array([center_position[0] - size/2,
#                                               center_position[1],
#                                               center_position[2]])
#                     left = Cube(size_y, left_position, face_colors[3])

#                     top_position = np.array([center_position[0],
#                                              center_position[1] + size/2,
#                                              center_position[2]])
#                     top = Cube(size_x, top_position, face_colors[4])

#                     bottom_position = np.array([center_position[0],
#                                                 center_position[1] - size/2,
#                                                 center_position[2]])
#                     bottom = Cube(size_x, bottom_position, face_colors[5])
                    
#                     self.cubes.append([center, front, back, right, left, top, bottom])
        
#         return self.cubes






