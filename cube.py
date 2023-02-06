from functools import cache

Cube = tuple[int, int, int]


@cache
def translated(cube: Cube, offset_x: int, offset_y: int, offset_z: int) -> Cube:
    x, y, z = cube
    return (x + offset_x, y + offset_y, z + offset_z)


@cache
def rotated_x(cube: Cube) -> Cube:
    x, y, z = cube
    return (x, -z, y)


@cache
def rotated_y(cube: Cube) -> Cube:
    x, y, z = cube
    return (z, y, -x)


@cache
def rotated_z(cube: Cube) -> Cube:
    x, y, z = cube
    return (-y, x, z)


@cache
def neighbors(cube: Cube) -> frozenset[Cube, Cube, Cube, Cube, Cube, Cube]:
    x, y, z = cube
    result = []
    result.append((x + 1, y, z))
    result.append((x - 1, y, z))
    result.append((x, y + 1, z))
    result.append((x, y - 1, z))
    result.append((x, y, z + 1))
    result.append((x, y, z - 1))
    return frozenset(result)
