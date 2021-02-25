import numpy as np
import matplotlib.pyplot as plt
import ast


def translate_x(l, times):
    out_list = []
    for v in l:
        v_out = v[:]
        v_out[0] += times
        out_list.append(v_out)
    return out_list


def translate_y(l, times):
    out_list = []
    for v in l:
        v_out = v[:]
        v_out[1] += times
        out_list.append(v_out)
    return out_list


def translate_z(l, times):
    out_list = []
    for v in l:
        v_out = v[:]
        v_out[2] += times
        out_list.append(v_out)
    return out_list


def rotate_x(l, times,  clockwise = True):
    clockwise_x_rotation = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
    anti_clockwise_x_rotation = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    if clockwise:
        return np.matmul(l, clockwise_x_rotation)
    else:
        return np.matmul(l, anti_clockwise_x_rotation)


def rotate_y(l,  clockwise = True):
    clockwise_y_rotation = [[0,0,-1], [0, 1, 0], [1, 0, 0]]
    anti_clockwise_y_rotation = [[0,0,1], [0, 1, 0], [-1, 0, 0]]
    if clockwise:
        return np.matmul(l, clockwise_y_rotation)
    else:
        return np.matmul(l, anti_clockwise_y_rotation)


def rotate_z(l, clockwise = True):
    clockwise_z_rotation = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    anti_clockwise_z_rotation = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

    if clockwise:
        return np.matmul(l, clockwise_z_rotation)
    else:
        return np.matmul(l, anti_clockwise_z_rotation)


def plot_cuboids(list_in, n, fig):
    colors = ["grey","forestgreen","limegreen","blue","royalblue","brown","violet","yellow","red"]
    dim = 5
    x, y, z = np.indices((dim, dim, dim))
    cubes = []
    voxels = None
    for v in list_in:
        cube = (x == v[0]) & (y == v[1]) & (z == v[2])
        cubes.append(cube)
        if voxels is None:
            voxels = cube
        else:
            voxels = voxels | cube
    if fig is None:
        fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors=colors[n], edgecolor='k')
    return fig


def plot_all(list_pieces):
    fig = None
    for n, piece in enumerate(list_pieces):
        fig = plot_cuboids(piece, n, fig)
    plt.show()
    pass


def read_files():
    out_list = []
    for i in range(1, 10):
        f = open("pieces/"+str(i)+".txt", "r")
        l = ast.literal_eval(f.readline())
        out_list.append(l)
    return out_list


def check_grid(l):
    grid_out = np.zeros([5,5,5])
    for p in l:
        for c in p:
            grid_out[c[0], c[1], c[2]] += 1
    print(grid_out)
    print((grid_out > 1).any())


def all_combinations(l):
    k = 0
    for p1
    for rotation_x in range(5):
        for rotation_y in range(5):
            for rotation_z in range(5):
                for translation_x in range(6):
                    for translation_y in range(6):
                        for translation_z in range(6):
                            k += 1
    print(k)



def main():
    all_combinations(2)
    pieces = read_files()
    check_grid(pieces)
    plt.show()


# main()
plot_all(read_files())
