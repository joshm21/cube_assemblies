from itertools import combinations

import cube as Cube
import orientation as Orientation
import piece as Piece
import files as Files

import plot as Plot


def generate_by_adding_cubes(
    max_cubes: int, search_space: list[Cube.Cube]
) -> list[Orientation.Orientation]:
    # https://math.stackexchange.com/a/4457462

    def recursively_add_cube(
        max_cubes: int,
        search_space: frozenset[Cube.Cube],
        results: list[Orientation.Orientation],
        polycube: Orientation.Orientation,
        untried_cubes: list[Cube.Cube],
    ) -> None:
        while untried_cubes:
            new_cube = untried_cubes.pop(0)
            new_polycube = frozenset((*polycube, new_cube))
            number_of_cubes = len(new_polycube)
            results.append(new_polycube)

            if number_of_cubes < max_cubes:
                new_untried = untried_cubes.copy()
                new_cube_neighbors = Cube.neighbors(new_cube)
                polycube_neighbors = Orientation.neighbors(polycube)
                new_allowed_neighbors = (
                    new_cube_neighbors.difference(polycube_neighbors)
                    .difference(polycube)
                    .intersection(search_space)
                )
                new_untried.extend(new_allowed_neighbors)
                recursively_add_cube(
                    max_cubes, search_space, results, new_polycube, new_untried
                )

    results = []
    polycube = frozenset()
    untried_cubes = [(0, 0, 0)]
    recursively_add_cube(max_cubes, search_space, results, polycube, untried_cubes)
    return results


def generate_by_combos(
    required: list[Cube.Cube], allowed: list[Cube.Cube]
) -> list[Orientation.Orientation]:
    results = []
    for number_chosen_cubes in range(1, len(allowed) + 1):
        for combo in combinations(allowed, number_chosen_cubes):
            orientation = (*required, *combo)
            if Orientation.is_connected(orientation):
                results.append(orientation)
    return results


def to_unique_pieces(
    orientations: list[Orientation.Orientation],
) -> set[Piece.Piece]:
    return {Piece.from_orientation(ort) for ort in orientations}


def generate_polyomino_orientations(max_cubes: int) -> list[Orientation.Orientation]:
    search_space = []
    for x in range(-max_cubes, max_cubes):
        for y in range(max_cubes):
            if y == 0 and x <= 0:
                continue
            search_space.append((x, y, 0))
    return generate_by_adding_cubes(max_cubes, search_space)


def generate_polycube_orientations(max_cubes: int) -> list[Orientation.Orientation]:
    search_space = []
    for x in range(-1, max_cubes):
        for y in range(-1, max_cubes):
            for z in range(-1, max_cubes):
                search_space.append((x, y, z))
    return generate_by_adding_cubes(max_cubes, search_space)


def generate_six_piece_burr_orientations() -> list[Orientation.Orientation]:

    required = [
        (0, 0, 0),
        (1, 0, 0),
        (4, 0, 0),
        (5, 0, 0),  # y=0, z=0
        (0, 1, 0),
        (1, 1, 0),
        (4, 1, 0),
        (5, 1, 0),  # y=1, z=0
        (0, 0, 1),
        (5, 0, 1),  # y=0, z=1
        (0, 1, 1),
        (5, 1, 1),  # y=1, z=1
    ]
    allowed = [
        (2, 0, 0),
        (3, 0, 0),  # y=0, z=0
        (2, 1, 0),
        (3, 1, 0),  # y=1, z=0
        (1, 0, 1),
        (2, 0, 1),
        (3, 0, 1),
        (4, 0, 1),  # y=0, z=1
        (1, 1, 1),
        (2, 1, 1),
        (3, 1, 1),
        (4, 1, 1),  # y=1, z=1
    ]
    return generate_by_combos(required, allowed)


def test_generators(polyomino_level: int, polycube_level: int) -> None:

    print("Testing Polyominoes...")
    # https://en.wikipedia.org/wiki/Polyomino#Enumeration_of_polyominoes
    fixed_polyominoes = (1, 2, 6, 19, 63, 216, 760, 2725, 9910, 36446, 135268, 505861)
    free_polyominoes = (1, 1, 2, 5, 12, 35, 108, 369, 1285, 4655, 17073, 63600)
    expected_fixed_polyominoes = sum(fixed_polyominoes[:polyomino_level])
    expected_free_polyominoes = sum(free_polyominoes[:polyomino_level])
    fixed_polyominoes = generate_polyomino_orientations(polyomino_level)
    free_polyominoes = to_unique_pieces(fixed_polyominoes)
    if expected_fixed_polyominoes != len(fixed_polyominoes):
        print(
            f" - expected {expected_fixed_polyominoes} fixed polyonomines, not {len(fixed_polyominoes)}"
        )
    if expected_free_polyominoes != len(free_polyominoes):
        print(
            f" - expected {expected_free_polyominoes} free polyonomines, not {len(free_polyominoes)}"
        )

    print("Testing Polycubes...")
    # https://en.wikipedia.org/wiki/Polycube#Enumerating_polycubes
    one_sided_polycubes = (1, 1, 2, 8, 29, 166, 1023, 6922)
    expected_polycubes = sum(one_sided_polycubes[:polycube_level])
    polycube_orientations = generate_polycube_orientations(polycube_level)
    polycube_pieces = to_unique_pieces(polycube_orientations)
    if expected_polycubes != len(polycube_pieces):
        print(f" - expected {expected_polycubes} polycubes, got {len(polycube_pieces)}")

    print("Testing Six Piece Burrs...")
    # https://billcutlerpuzzles.com/docs/CA6PB/pieces.html
    expected_burr_orientations = 2225
    expected_burr_pieces = 837
    burr_orientations = generate_six_piece_burr_orientations()
    burr_pieces = to_unique_pieces(burr_orientations)
    if expected_burr_orientations != len(burr_orientations):
        print(
            f" - expected {expected_burr_orientations} burr orientations, got {len(burr_orientations)}"
        )
    if expected_burr_pieces != len(burr_pieces):
        print(f" - expected {expected_burr_pieces} burr pieces, got {len(burr_pieces)}")


def save_generated_pieces(polyomino_level: int, polycube_level: int) -> None:
    Files.save_pieces(
        "generated_polyomino_pieces.txt",
        to_unique_pieces(generate_polyomino_orientations(polycube_level)),
    )
    Files.save_pieces(
        "generated_polycube_pieces.txt",
        to_unique_pieces(generate_polycube_orientations(polycube_level)),
    )
    Files.save_pieces(
        "generated_burr_pieces.txt",
        to_unique_pieces(generate_six_piece_burr_orientations()),
    )


def pentacubes():
    # https://puzzler.sourceforge.net/docs/polycubes-intro.html
    pentacubes = (
        frozenset(((0, 0, 0), (0, 1, 0), (0, 1, 1), (1, 1, 1), (1, 0, 1))),
        frozenset(((0, 0, 1), (1, 0, 0), (1, 0, 1), (1, 0, 2), (2, 0, 2))),
        frozenset(((0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4))),
        frozenset(((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2), (1, 1, 2))),
        frozenset(((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2), (1, 1, 1))),
        frozenset(((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2), (1, 0, 0))),
        frozenset(((0, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3))),
        frozenset(((0, 0, 2), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2))),
        frozenset(((0, 0, 1), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2))),
        frozenset(((0, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2))),
        frozenset(((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2))),
        frozenset(((0, 0, 1), (1, 0, 1), (1, 0, 0), (2, 0, 0), (3, 0, 0))),
        frozenset(((0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 1, 0), (2, 1, 0))),
        frozenset(((1, 0, 1), (0, 1, 1), (1, 1, 1), (1, 1, 0), (2, 1, 0))),
        frozenset(((0, 0, 0), (0, 0, 1), (0, 0, 2), (1, 0, 1), (1, 0, 2))),
        frozenset(((1, 0, 0), (0, 1, 0), (0, 1, 1), (1, 1, 0), (1, 1, 1))),
        frozenset(((0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1))),
        frozenset(((1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1))),
        frozenset(((0, 0, 2), (1, 0, 2), (2, 0, 2), (1, 0, 0), (1, 0, 1))),
        frozenset(((1, 0, 1), (0, 1, 1), (1, 1, 0), (1, 1, 1), (2, 1, 1))),
        frozenset(((1, 0, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1), (2, 1, 1))),
        frozenset(((0, 0, 1), (0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 1))),
        frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 1), (2, 0, 2))),
        frozenset(((0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 2, 0))),
        frozenset(((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1))),
        frozenset(((0, 0, 0), (1, 0, 0), (1, 0, 1), (2, 0, 1), (2, 0, 2))),
        frozenset(((0, 0, 1), (1, 0, 0), (1, 0, 1), (1, 0, 2), (2, 0, 1))),
        frozenset(((0, 0, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3))),
        frozenset(((0, 0, 2), (1, 0, 2), (1, 0, 1), (1, 0, 0), (2, 0, 0))),
    )
    for ort in pentacubes:
        Plot.plot(ort)


def main():
    # save_generated_pieces(10, 6)
    save_generated_pieces(10, 6)


if __name__ == "__main__":
    main()
