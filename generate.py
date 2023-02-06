from itertools import combinations

import cube as Cube
import orientation as Orientation
import piece as Piece


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
            orientation = frozenset((*required, *combo))
            if Orientation.is_connected(orientation):
                results.append(orientation)
    return results


def to_unique_pieces(
    orientations: list[Orientation.Orientation],
) -> set[Piece.Piece]:
    return {Piece.from_orientation(ort) for ort in orientations}


def main():
    # save_generated_pieces(10, 6)
    save_generated_pieces(10, 6)


if __name__ == "__main__":
    main()
