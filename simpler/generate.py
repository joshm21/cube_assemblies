import cube as Cb
import orientation as Ort


def generate_by_adding_cubes(
    max_cubes: int, max_x: int, max_y: int, max_z: int
) -> set[Ort.Orientation]:
    def precompute_neighbors_and_rotations(max_x: int, max_y: int, max_z: int):
        precomputed_results = {}
        possible_cubes = tuple(
            (x, y, z)
            for x in range(max_x + 1)
            for y in range(max_y + 1)
            for z in range(max_z + 1)
        )
        for cube in possible_cubes:
            precomputed_results[cube] = {
                "neighbors": Cb.get_neighbors_within_limits(cube, max_x, max_y, max_z),
                "rotations": {
                    "x": Cb.rotated_x(cube),
                    "y": Cb.rotated_y(cube),
                    "z": Cb.rotated_z(cube),
                },
            }
        return precomputed_results

    def get_children(ort: Ort.Orientation, precomputed: dict) -> list[Ort.Orientation]:
        children = []
        for cube in current_ort:
            for neighbor in precomputed[cube]["neighbors"].difference(current_ort):
                new_ort = Ort.translated_to_origin((neighbor, *current_ort))
                if Ort.max_x(new_ort) > max_x:
                    continue
                if Ort.max_y(new_ort) > max_y:
                    continue
                if Ort.max_z(new_ort) > max_z:
                    continue
                children.append(new_ort)
        return children

    precomputed = precompute_neighbors_and_rotations(max_x, max_y, max_z)
    seen_orienations = set()
    queue = [frozenset(((0, 0, 0),))]
    while queue:
        current_ort = queue.pop(0)
        number_of_cubes = len(current_ort)
        if number_of_cubes > max_cubes:
            break
        seen_orienations.add(current_ort)
        queue.extend(get_children(current_ort, precomputed))
    return seen_orienations


def generate_polyominos(max_cubes: int) -> set[Ort.Orientation]:
    return generate_by_adding_cubes(max_cubes, max_cubes - 1, max_cubes - 2, 0)


def generate_polycubes(max_cubes: int) -> set[Ort.Orientation]:
    return generate_by_adding_cubes(
        max_cubes, max_cubes - 1, max_cubes - 2, max_cubes - 3
    )


def generate_burr() -> set[Ort.Orientation]:
    generated = generate_by_adding_cubes(24, 5, 1, 1)
    # then filter out those that don't have "always cubes"
    return generated


def main():
    results = generate_polyominos(6)
    print(len(results))


if __name__ == "__main__":
    main()
