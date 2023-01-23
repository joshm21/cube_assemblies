from itertools import combinations
from piece import Piece


def generate_by_adding_cubes():
    # can't just go from last added cube, or some will be missed
    # need to go from all cubes to all legal neighbors

    # pass a dict mapping xyz to neighbors to get children
    # don't need get children function, just dict
    pass


def generate_by_combinations():
    # like burr
    pass


def generate_pieces(
    required_xyzs: tuple[tuple[int, int, int]],
    allowed_xyzs: tuple[tuple[int, int, int]],
    max_allowed_xyzs: int,
) -> set[Piece]:
    """Generate pieces by combining required_xyzs with all combinations of allowed_xyzs"""

    def is_connected(xyzs: tuple[tuple[int, int, int]]) -> bool:
        """Is every xyz (in)directly connected to every other xyz? (orthagonal not diagonal)
        ie the set of xyzs is a connected, undirected graph"""

        def map_xyz_to_neighbors(xyzs: tuple[tuple[int, int, int]]) -> dict:
            map_dict = {}
            for x, y, z in xyzs:
                neighbors = []
                if (x + 1, y, z) in xyzs:
                    neighbors.append((x + 1, y, z))
                if (x - 1, y, z) in xyzs:
                    neighbors.append((x - 1, y, z))
                if (x, y + 1, z) in xyzs:
                    neighbors.append((x, y + 1, z))
                if (x, y - 1, z) in xyzs:
                    neighbors.append((x, y - 1, z))
                if (x, y, z + 1) in xyzs:
                    neighbors.append((x, y, z + 1))
                if (x, y, z - 1) in xyzs:
                    neighbors.append((x, y, z - 1))
                map_dict[(x, y, z)] = tuple(neighbors)
            return map_dict

        def depth_first_search(
            start_xyz: tuple[int, int, int], neighbors: dict, visited: set
        ) -> None:
            visited.add(start_xyz)
            for neighbor in neighbors[start_xyz]:
                if neighbor not in visited:
                    depth_first_search(neighbor, neighbors, visited)

        neighbors = map_xyz_to_neighbors(xyzs)
        visited = set()
        depth_first_search(xyzs[0], neighbors, visited)
        if set(xyzs) == visited:
            return True
        return False

    seen_pieces = set()

    for number_of_allowed_xyzs in range(max_allowed_xyzs):
        for combo in combinations(allowed_xyzs, number_of_allowed_xyzs + 1):
            all_xyzs = (*required_xyzs, *combo)
            if is_connected(all_xyzs):
                seen_pieces.add(Piece.from_xyzs(all_xyzs))
    return seen_pieces


def generate_polyominos(max_number_of_cubes: int) -> None:
    # https://en.wikipedia.org/wiki/Polyomino#Enumeration_of_polyominoes
    allowed_xyzs = []
    for x in range(max_number_of_cubes):
        for y in range(max_number_of_cubes - 1):
            allowed_xyzs.append((x, y, 0))
    pieces = generate_pieces((), tuple(allowed_xyzs), max_number_of_cubes)
    return pieces


def generate_polycubes(max_number_of_cubes: int) -> None:
    # https://en.wikipedia.org/wiki/Polycube#Enumerating_polycubes
    allowed_xyzs = []
    for x in range(max_number_of_cubes):
        for y in range(max_number_of_cubes - 1):
            for z in range(max_number_of_cubes - 2):
                allowed_xyzs.append((x, y, z))
    pieces = generate_pieces((), tuple(allowed_xyzs), max_number_of_cubes)
    return pieces


def generate_six_piece_burr() -> None:
    pass


def main():
    print(len(generate_polycubes(4)))
    # about 5 seconds


if __name__ == "__main__":
    main()
