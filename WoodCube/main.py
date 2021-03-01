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
        return np.matmul(l, clockwise_x_rotation).tolist()
    else:
        return np.matmul(l, anti_clockwise_x_rotation).tolist()


def rotate_y(l,  clockwise = True):
    clockwise_y_rotation = [[0,0,-1], [0, 1, 0], [1, 0, 0]]
    anti_clockwise_y_rotation = [[0,0,1], [0, 1, 0], [-1, 0, 0]]
    if clockwise:
        return np.matmul(l, clockwise_y_rotation).tolist()
    else:
        return np.matmul(l, anti_clockwise_y_rotation).tolist()


def rotate_z(l, clockwise = True):
    clockwise_z_rotation = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    anti_clockwise_z_rotation = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

    if clockwise:
        return np.matmul(l, clockwise_z_rotation).tolist()
    else:
        return np.matmul(l, anti_clockwise_z_rotation).tolist()


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


def get_grid (l):
    grid_out = np.zeros([5, 5, 5])
    for p in l:
        for c in p:
            grid_out[c[0], c[1], c[2]] += 1
    return grid_out


def check_grid(l):
    return not (get_grid(l) > 1).any()


def check(list_in):
    too_large = any(any(x > 4 for x in sublist) for sublist in list_in)
    too_small = any(any(x < 0 for x in sublist) for sublist in list_in)
    return(too_large or too_small)


def all_combinations(l, number_of_pieces, i=0, good_pieces=[]):
    good_pieces_c = good_pieces[:]
    k = 0
    if not i >= number_of_pieces:
        for rotation_x in range(5):
            for rotation_y in range(5):
                for rotation_z in range(5):
                    for translation_x in range(5):
                        for translation_y in range(5):
                            for translation_z in range(5):
                                piece = rotate_x(l[i], rotation_x)
                                piece = rotate_y(piece, rotation_y)
                                piece = rotate_z(piece, rotation_z)
                                piece = translate_x(piece, translation_x)
                                piece = translate_y(piece, translation_y)
                                piece = translate_z(piece, translation_z)
                                if not check(piece):
                                    k += 1

                                    good_pieces_c.append(piece)
                                    all_combinations(l, number_of_pieces, i+1, good_pieces_c)
                                    if i == number_of_pieces-1 and check_grid(good_pieces_c):
                                        print("")
                                        print("Last piece:", i)
                                        print(good_pieces_c)
                                        print("Number of good pieces:", len(good_pieces_c))
                                        print(get_grid(good_pieces_c))
                                        print(check_grid(good_pieces_c))
                                        # plot_all(good_pieces_c)
                                    del good_pieces_c[-1]


def main():
    pieces = read_files()
    n = 2
    pieces = pieces[:n]
    all_combinations(pieces, n)
    check_grid(pieces)
    plt.show()


# main()
# plot_all(read_files())

print(check_grid([[[0,3,2]]]))
