import numpy as np
import matplotlib.pyplot as plt


class Plot:
    pass

    # add pieces with color
    # setup axes
    # plot


def plot(points):

    # points = (2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)  # normalized 1
    # points = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0))  # normalized 2

    # only in 1
    # points = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 1))  #L
    # points = ((0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 2, 1))  #L
    # points = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 0, 1))  # L
    # points = ((0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 0, 1))  # L
    # # only in 2
    # points = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 2, 0)) #L
    # points = ((0, 0, 0), (0, 1, 0), (0, 2, 0), (1, 2, 0))
    # points = ((2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0))
    # points = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0))

    # points = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0)) # S
    # points = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0))  # L
    # points = ((1, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)) # T
    # points = ((2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0))  # L
    # points = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0))
    # points = ((1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0))
    # points = ((0, 1, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1))
    # points = ((1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1))
    # points = ((1, 0, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1))
    # points = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0))

    # missing V and X

    x_max = 6
    y_max = 6
    z_max = 6
    for point in points:
        if point[0] >= x_max:
            x_max = point[0] + 3
        if point[1] >= y_max:
            y_max = point[1] + 3
        if point[2] >= z_max:
            z_max = point[2] + 3

    # format axes
    ax = plt.figure().add_subplot(projection="3d")
    ax.set_xlabel('x')
    ax.set_xticks([x+0.5 for x in range(0, x_max)])
    ax.set_xticklabels([str(x) for x in range(0, x_max)])
    ax.set_ylabel('y')
    ax.set_yticks([y+0.5 for y in range(0, y_max)])
    ax.set_yticklabels([str(y) for y in range(0, y_max)])
    ax.set_zlabel('z')
    ax.set_zticks([z+0.5 for z in range(0, z_max)])
    ax.set_zticklabels([str(z) for z in range(0, z_max)])
    ax.set_box_aspect(aspect=(1, 1, 1))

    voxels = np.zeros((x_max, y_max, z_max))
    for point in points:
        voxels[point] = True

    ax.voxels(voxels, edgecolor="k")
    plt.show()


def main():

    orientations = (
        ((2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)),  # L
        ((1, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)),  # T
        ((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)),  # O
        ((0, 1, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1)),  # a
        ((1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)),  # a
        ((1, 0, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1)),  # a
        ((0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0)),  # a
        ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)),  # a
    )
    for orientation in orientations:
        plot(orientation)


if __name__ == '__main__':
    main()
