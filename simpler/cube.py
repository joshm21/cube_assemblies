Cube = tuple[int, int, int]


def translated(cube: Cube, x_shift: int, y_shift: int, z_shift: int) -> Cube:
    x, y, z = cube
    return (x + x_shift, y + y_shift, z + z_shift)


def rotated_x(cube: Cube) -> Cube:
    x, y, z = cube
    return (x, -z, y)


def rotated_y(cube: Cube) -> Cube:
    x, y, z = cube
    return (z, y, -x)


def rotated_z(cube: Cube) -> Cube:
    x, y, z = cube
    return (-y, x, z)


def get_all_neighbors(cube: Cube) -> tuple[Cube, Cube, Cube, Cube, Cube, Cube]:
    x, y, z = cube
    neighbors = []
    neighbors.append((x + 1, y, z))
    neighbors.append((x - 1, y, z))
    neighbors.append((x, y + 1, z))
    neighbors.append((x, y - 1, z))
    neighbors.append((x, y, z + 1))
    neighbors.append((x, y, z - 1))
    return tuple(neighbors)


def get_neighbors_within_limits(
    cube: Cube, max_x: int, max_y: int, max_z: int
) -> frozenset[Cube]:
    within_limits = []
    for x, y, z in get_all_neighbors(cube):
        if x > max_x:
            continue
        if y > max_y:
            continue
        if z > max_z:
            continue
        within_limits.append((x, y, z))
    return frozenset(within_limits)


if __name__ == "__main__":
    print("cube")
