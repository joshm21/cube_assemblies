from . import orientation as Orientation
from .generate import generate_by_adding_cubes, to_unique_pieces


def generate_polyomino_orientations(max_cubes: int) -> list[Orientation.Orientation]:
    search_space = []
    for x in range(-max_cubes, max_cubes):
        for y in range(max_cubes):
            if y == 0 and x <= 0:
                continue
            search_space.append((x, y, 0))
    return generate_by_adding_cubes(max_cubes, search_space)
