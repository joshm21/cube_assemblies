import orientation as Orientation
from generate import generate_by_adding_cubes, to_unique_pieces


def generate_polyomino_orientations(max_cubes: int) -> list[Orientation.Orientation]:
    search_space = []
    for x in range(-max_cubes, max_cubes):
        for y in range(max_cubes):
            if y == 0 and x <= 0:
                continue
            search_space.append((x, y, 0))
    return generate_by_adding_cubes(max_cubes, search_space)


def test(max_cubes: int) -> None:
    # https://en.wikipedia.org/wiki/Polyomino#Enumeration_of_polyominoes
    print("Testing polyominoes...")

    fixed_polyominoes = (1, 2, 6, 19, 63, 216, 760, 2725, 9910, 36446, 135268, 505861)
    free_polyominoes = (1, 1, 2, 5, 12, 35, 108, 369, 1285, 4655, 17073, 63600)
    expected_fixed_polyominoes = sum(fixed_polyominoes[:max_cubes])
    expected_free_polyominoes = sum(free_polyominoes[:max_cubes])
    fixed_polyominoes = generate_polyomino_orientations(max_cubes)
    free_polyominoes = to_unique_pieces(fixed_polyominoes)
    print(
        f"Generating correct fixed counts? {expected_fixed_polyominoes == len(fixed_polyominoes)}"
    )
    print(
        f"Generating correct free counts? {expected_free_polyominoes == len(free_polyominoes)}"
    )


def main() -> None:
    test(8)


if __name__ == "__main__":
    main()
