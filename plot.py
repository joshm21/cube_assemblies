import numpy as np
import matplotlib.pyplot as plt


def plot(points):

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
    ax.set_xlabel("x")
    ax.set_xticks([x + 0.5 for x in range(0, x_max)])
    ax.set_xticklabels([str(x) for x in range(0, x_max)])
    ax.set_ylabel("y")
    ax.set_yticks([y + 0.5 for y in range(0, y_max)])
    ax.set_yticklabels([str(y) for y in range(0, y_max)])
    ax.set_zlabel("z")
    ax.set_zticks([z + 0.5 for z in range(0, z_max)])
    ax.set_zticklabels([str(z) for z in range(0, z_max)])
    ax.set_box_aspect(aspect=(1, 1, 1))

    voxels = np.zeros((x_max, y_max, z_max))
    for point in points:
        voxels[point] = True

    ax.voxels(voxels, edgecolor="k")
    plt.show()


def main():

    orientations = ()
    for orientation in orientations:
        plot(orientation)


if __name__ == "__main__":
    main()
