import numpy as np
import matplotlib.pyplot as plt


class Plot:

    def __init__(self, x_max, y_max, z_max) -> None:
        self.ax = plt.figure().add_subplot(projection='3d')
        self.ax.set_box_aspect(aspect=(1, 1, 1))
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')

    # def format_axes(self):
        #
        # ax.set_xticks([x+0.5 for x in range(0, x_max)])
        # ax.set_xticklabels([str(x) for x in range(0, x_max)])
        # ax.set_ylabel("y")
        # ax.set_yticks([y+0.5 for y in range(0, y_max)])
        # ax.set_yticklabels([str(y) for y in range(0, y_max)])
        # ax.set_zlabel("z")
        # ax.set_zticks([z+0.5 for z in range(0, z_max)])
        # ax.set_zticklabels([str(z) for z in range(0, z_max)])


def setup(x_max, y_max, z_max):
    pass


def add_piece(piece, color):
    pass


def plot():
    """Plots the polycube in 3d space using Matplotlib Voxels"""

    # x_max = max([cube.x for cube in self]) + 1
    # y_max = max([cube.y for cube in self]) + 1
    # z_max = max([cube.z for cube in self]) + 1

    x_max = 5
    y_max = 5
    z_max = 5

    ax = plt.figure().add_subplot(projection="3d")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    voxels = np.zeros((x_max, y_max, z_max))
    voxels[(-1, 0, 0)] = True

    # for cube in self:
    #     coords = (cube.x, cube.y, cube.z)
    #     voxels[coords] = True

    ax.voxels(voxels, edgecolor="k")
    plt.show()


if __name__ == '__main__':
    plot()
