import cube as Cube

Orientation = frozenset[Cube.Cube]


def translated(
    orientation: Orientation, offset_x: int, offset_y: int, offset_z: int
) -> Orientation:
    return frozenset(
        Cube.translated(cube, offset_x, offset_y, offset_z) for cube in orientation
    )


def translated_to_origin(orientation: Orientation) -> Orientation:
    min_x = min((cube[0] for cube in orientation))
    min_y = min((cube[1] for cube in orientation))
    min_z = min((cube[2] for cube in orientation))
    return translated(orientation, -min_x, -min_y, -min_z)


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

    def depth_first_search(start: Cube, neighbors: dict, visited: set) -> None:
        visited.add(start)
        for neighbor in neighbors[start]:
            if neighbor not in visited:
                depth_first_search(neighbor, neighbors, visited)

    neighbors = map_cube_to_other_cubes(orientation)
    visited = set()
    depth_first_search(orientation[0], neighbors, visited)
    if set(orientation) == visited:
        return True
    return False


def is_millable(orientation: Orientation) -> bool:
    # no internal corners, where the sides of three cubes meet inside the piece in a concave fashion
    pass


def is_notchable(orientation: Orientation) -> bool:
    # no concave crosscuts perpendicular to the axis
    pass
