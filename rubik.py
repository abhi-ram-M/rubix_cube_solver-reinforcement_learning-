import pyray as pr
import numpy as np
import random

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
    
    def rotate(self, axis, theta):
        if axis == 0 :
            rotation_matrix = np.array([
                [1,0,0],
                [0,np.cos(theta),-np.sin(theta)],
                [0,np.sin(theta),np.cos(theta)]
            ])
        elif axis ==1:
            rotation_matrix = np.array([
                [np.cos(theta),0,np.sin(theta)],
                [0,1,0],
                [-np.sin(theta),0,np.cos(theta)]
            ])
        elif axis ==2:
            rotation_matrix = np.array([
                [np.cos(theta), -np.sin(theta),0],
                [np.sin(theta),np.cos(theta),0],
                [0,0,1]
            ])
        else:
            raise ValueError("Invallid axis. Use 'x' , 'y' or 'z' . ")
        self.center = rotation_matrix @ self.center

        self.orientation = rotation_matrix @ self.orientation

    def get_rotation_axis_angle(self):
        angle = np.arccos((np.trace(self.orientation)-1)/2)
        if angle == 0 :
            axis = np.array([0,0,0])
        else:
            rx = self.orientation[2,1] - self.orientation[1,2]
            ry = self.orientation[0,2] - self.orientation[2,0]
            rz = self.orientation[1,0] - self.orientation[0,1]
            axis = np.array([rx,ry,rz]) / (2*np.sin(angle))
        axis = pr.Vector3(axis[0],axis[1],axis[2])
        return axis, np.degrees(angle)




class Rubik:
    def __init__(self) -> None:
        self.cubes = []

        self.is_rotating = False
        self.rotation_angle = 0
        self.rotation_axis = None
        self.level =None
        self.segment = None
        self.target_rotation = 0
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
    

    def choose_piece(self, piece, axis_index, level):
        if level == 0 and round(piece[0].center[axis_index],1)<0:
            return True
        elif level == 1 and round(piece[0].center[axis_index],1)==0:
            return True
        elif level == 2 and round(piece[0].center[axis_index],1)>0:
            return True
        return False
    

    def get_face(self,axis, level) :
        axis_index = np.nonzero(axis)[0][0]
        segment = [i for i, cube in enumerate(self.cubes)\
                   if self.choose_piece(cube, axis_index, level)]
        return segment

    def handle_rotation(self,rotation_queue, animation_step=None):
        if rotation_queue and not self.is_rotating:
            self.target_rotation,self.rotation_axis, self.level = rotation_queue.pop(0)
            if self.target_rotation >0:
                self.target_rotation += random.uniform(0,1) * 10**-3
            else:
                self.target_rotation -= random.uniform(0,1)*10**-3
            
            
            self.segment = self.get_face(self.rotation_axis, self.level)
            self.rotation_angle = 0
            self.is_rotating = True

        if self.is_rotating:
            if (self.rotation_angle != self.target_rotation):
                diff = abs(self.target_rotation - self.rotation_angle)
                delta_angle = min(np.radians(1),diff)
#
                self.rotation_angle += delta_angle if self.target_rotation > 0 else -delta_angle
            else:
                delta_angle = 0
                self.is_rotating = False
                if animation_step is not None:
                    animation_step += 1
            
            for id,cube in enumerate(self.cubes):
                self.rotation_axis = np.atleast_1d(self.rotation_axis)
                nonzero_indices = np.nonzero(self.rotation_axis)[0]
                if len(nonzero_indices) == 0:
                    raise ValueError(f"rotation_axis is invalid for rotation: {self.rotation_axis}")
                axis_index = nonzero_indices[0]
                if id in self.segment:
                    for part_id, _ in enumerate(cube):
                        if self.target_rotation > 0:
                            self.cubes[id][part_id].rotate(axis_index, delta_angle)
                        else:
                            self.cubes[id][part_id].rotate(axis_index, -delta_angle)

                        pos_x,pos_y,pos_z = self.cubes[id][part_id].center

                        translation = pr.matrix_translate(pos_x, pos_y, pos_z)
                        rota, angle = self.cubes[id][part_id].get_rotation_axis_angle()
                        rotation = pr.matrix_rotate(rota, np.radians(angle))
                        transform = pr.matrix_multiply(rotation, translation)
                        self.cubes[id][part_id].model.transform = transform
        else:
            self.is_rotating = True
        
        return rotation_queue, animation_step






