import numpy as np

z_rotation = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]

v_new = np.matmul([1,1,2],z_rotation)
print(v_new)
v_new = np.matmul(v_new, z_rotation)
print(v_new)
v_new = np.matmul(v_new, z_rotation)
print(v_new)
v_new = np.matmul(v_new, z_rotation)
print(v_new)

class pieces:
    def __init__(self):
        self.coordinate_list = []

    def add_coordinate(self, x, y, z):
        self.coordinate_list.append([x, y, z])

    def rotate_x(self,  clockwise = True):
        clockwise_x_rotation = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
        anti_clockwise_x_rotation = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
        if clockwise:
            return np.matmul(self.coordinate_matrix, clockwise_x_rotation)
        else:
            return np.matmul(self.coordinate_matrix, anti_clockwise_x_rotation)

    def rotate_y(self,  clockwise = True):
        clockwise_y_rotation = [[0,0,-1], [0, 1, 0], [1, 0, 0]]
        anti_clockwise_y_rotation = [[0,0,1], [0, 1, 0], [-1, 0, 0]]
        if clockwise:
            return np.matmul(self.coordinate_matrix, clockwise_y_rotation)
        else:
            return np.matmul(self.coordinate_matrix, anti_clockwise_y_rotation)

    def rotate_z(self, clockwise = True):
        clockwise_z_rotation = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
        anti_clockwise_z_rotation = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        if clockwise:
            return np.matmul(self.coordinate_matrix, clockwise_z_rotation)
        else:
            return np.matmul(self.coordinate_matrix, anti_clockwise_z_rotation)

    def __str__(self):
        return str(self.coordinate_matrix)


# p_test = pieces([[1,0,0,0,1], [1,0,0,0,0], [1,0,0,0,0], [1,1,1,1,1]])
# print(p_test)
# p_test.rotate_x()
# print(p_test)

p_1 = pieces()

print(np.matmul([[1,0,0,1], [1,0,1,0,], [1,1,0,0,], [1,1,1,1]],[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]))
