from . import cube as Cube


Orientation = frozenset[Cube.Cube]


def max_x(orientation: Orientation) -> int:
    return max(cube[0] for cube in orientation)


def max_y(orientation: Orientation) -> int:
    return max(cube[1] for cube in orientation)


def max_z(orientation: Orientation) -> int:
    return max(cube[2] for cube in orientation)


def min_x(orientation: Orientation) -> int:
    return min(cube[0] for cube in orientation)


def min_y(orientation: Orientation) -> int:
    return min(cube[1] for cube in orientation)


def min_z(orientation: Orientation) -> int:
    return min(cube[2] for cube in orientation)


def translated(
    orientation: Orientation, offset_x: int, offset_y: int, offset_z: int
) -> Orientation:
    return frozenset(
        Cube.translated(cube, offset_x, offset_y, offset_z) for cube in orientation
    )


def translated_to_origin(orientation: Orientation) -> Orientation:
    return translated(
        orientation, -min_x(orientation), -min_y(orientation), -min_z(orientation)
    )


def rotated_x(orientation: Orientation) -> Orientation:
    return frozenset(Cube.rotated_x(cube) for cube in orientation)


def rotated_y(orientation: Orientation) -> Orientation:
    return frozenset(Cube.rotated_y(cube) for cube in orientation)


def rotated_z(orientation: Orientation) -> Orientation:
    return frozenset(Cube.rotated_z(cube) for cube in orientation)


def neighbors(orientation: Orientation) -> frozenset[Cube.Cube]:
    return frozenset().union(*[Cube.neighbors(cube) for cube in orientation])


def is_connected(orientation: Orientation) -> bool:
    """Is every cube connected to every other cube? (orthagonal not diagonal)
    ie the set of cubes is a connected, undirected graph"""

    def map_cube_to_other_cubes(orientation: Orientation) -> dict:
        results = {}
        for cube in orientation:
            all_cube_neighbors = Cube.neighbors(cube)
            only_neighbors_in_polycube = all_cube_neighbors.intersection(orientation)
            results[cube] = only_neighbors_in_polycube
        return results

    def depth_first_search(start: Cube, neighbors_map: dict, visited: set) -> None:
        visited.add(start)
        for neighbor in neighbors_map[start]:
            if neighbor not in visited:
                depth_first_search(neighbor, neighbors_map, visited)

    neighbors_map = map_cube_to_other_cubes(orientation)
    visited = set()
    depth_first_search(next(iter(orientation)), neighbors_map, visited)
    if set(orientation) == visited:
        return True
    return False


def is_notchable(orientation: Orientation) -> bool:
    """Is orientation makeable with continuous cuts along the 3 axes? (e.g.with a dado stack)
    If any cube is cut out, to be notchable one of the following must be true
        1. all cubes above and below are also cut out
        2. all cubes left or right are also cut out
        3. all cubes front or back are also cut out"""
    x_min = min_x(orientation)
    x_max = max_x(orientation)
    y_min = min_y(orientation)
    y_max = max_y(orientation)
    z_min = min_z(orientation)
    z_max = max_z(orientation)
    # loop through all cubes in bounding box of orientation
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                if (x, y, z) in orientation:
                    continue  # if cube exists, then skip, else...
                cubes_above_below = {
                    (x, y, z_varies) for z_varies in range(z_min, z_max + 1)
                }
                cubes_left_right = {
                    (x_varies, y, z) for x_varies in range(x_min, x_max + 1)
                }
                cubes_front_back = {
                    (x, y_varies, z) for y_varies in range(y_min, y_max + 1)
                }

                no_cubes_above_below = cubes_above_below.isdisjoint(orientation)
                no_cubes_left_right = cubes_left_right.isdisjoint(orientation)
                no_cubes_front_back = cubes_front_back.isdisjoint(orientation)
                if not any(
                    [no_cubes_above_below, no_cubes_left_right, no_cubes_front_back]
                ):
                    return False
    return True


def is_millable(orientation: Orientation) -> bool:
    # no internal corners, where the sides of three cubes meet inside the piece in a concave fashion
    pass
