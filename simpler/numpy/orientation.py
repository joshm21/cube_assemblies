import numpy as np

Orientation = np.ndarray[(int, int, int), np.bool_]


def to_tuples(ort: Orientation) -> tuple[tuple[tuple[bool, bool, bool]]]:
    shape = ort.shape
    results = []
    for x_ndx in range(shape[0]):
        x_list = []
        for y_ndx in range(shape[1]):
            x_list.append(tuple(ort[x_ndx][y_ndx]))
        results.append(tuple(x_list))
    return tuple(results)


def rotated_x(ort: Orientation) -> Orientation:
    return np.rot90(ort.copy(), k=1, axes=(1, 2))


def rotated_y(ort):
    return np.rot90(ort.copy(), k=1, axes=(2, 0))


def rotated_z(ort):
    return np.rot90(ort.copy(), k=1, axes=(0, 1))


def number_of_cubes(ort: Orientation) -> int:
    return np.sum(ort)


def get_polyomino_orientations(ort: Orientation) -> tuple[Orientation]:
    rot000 = ort
    rot090 = rotated_z(rot000)
    rot180 = rotated_z(rot090)
    rot270 = rotated_z(rot180)
    flp000 = rotated_x(rotated_x(rot000))
    flp090 = rotated_z(flp000)
    flp180 = rotated_z(flp090)
    flp270 = rotated_z(flp180)
    return (rot000, rot090, rot180, rot270, flp000, flp090, flp180, flp270)


def get_polyomino_children(
    ort: Orientation, bounding_box: Orientation
) -> set[Orientation]:
    children = []
    for cube in np.nditer(ort):
        if not cube:
            continue
        


def get_polycube_orientations(ort: Orientation) -> set[Orientation]:
    pass


def get_burr_orientations(ort: Orientation) -> set[Orientation]:
    pass


def has_cube(ort: Orientation, x: int, y: int, z: int) -> bool:
    return ort[x][y][z]


if __name__ == "__main__":
    matrix = np.arange(27).reshape(3, 3, 3)
    print(matrix)
    print("~~~~~~~~~~~~~~~")
    tups = to_tuples(matrix)
    for item in tups:
        print(item)
