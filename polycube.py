from . import orientation as Orientation
from .generate import generate_by_adding_cubes, to_unique_pieces


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


def generate_polycube_orientations(max_cubes: int) -> list[Orientation.Orientation]:
    search_space = []
    for x in range(-1, max_cubes):
        for y in range(-1, max_cubes):
            for z in range(-1, max_cubes):
                search_space.append((x, y, z))
    return generate_by_adding_cubes(max_cubes, search_space)


def test(max_cubes: int):
    # https://en.wikipedia.org/wiki/Polycube#Enumerating_polycubes
    print("Testing polycubes...")

    one_sided_polycubes = (1, 1, 2, 8, 29, 166, 1023, 6922)
    expected_polycubes = sum(one_sided_polycubes[:max_cubes])
    polycube_orientations = generate_polycube_orientations(max_cubes)
    polycube_pieces = to_unique_pieces(polycube_orientations)
    print(f"Generating correct counts? {expected_polycubes == len(polycube_pieces)}")


def main():
    test(5)


if __name__ == "__main__":
    main()
