import cube as Cb

Orientation = frozenset[Cb.Cube]


def min_x(ort: Orientation) -> int:
    return min((x for x, y, z in ort))


def min_y(ort: Orientation) -> int:
    return min((y for x, y, z in ort))


def min_z(ort: Orientation) -> int:
    return min((z for x, y, z in ort))


def max_x(ort: Orientation) -> int:
    return max((x for x, y, z in ort))


def max_y(ort: Orientation) -> int:
    return max((y for x, y, z in ort))


def max_z(ort: Orientation) -> int:
    return max((z for x, y, z in ort))


def translated_to_origin(ort: Orientation) -> Orientation:
    x_offset = min_x(ort) * -1
    y_offset = min_y(ort) * -1
    z_offset = min_z(ort) * -1
    return frozenset(
        (Cb.translated(cube, x_offset, y_offset, z_offset) for cube in ort)
    )


def rotated_x(ort: Orientation) -> Orientation:
    return frozenset((Cb.rotated_x(cube) for cube in ort))


def rotated_y(ort: Orientation) -> Orientation:
    return frozenset((Cb.rotated_y(cube) for cube in ort))


def rotated_z(ort: Orientation) -> Orientation:
    return frozenset((Cb.rotated_z(cube) for cube in ort))


if __name__ == "__main__":
    print("orientation")
