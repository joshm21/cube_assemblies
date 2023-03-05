import json

import piece
import orientation
import plot

BOARD_WIDTH = 20
BOARD_HEIGHT = 20

# https://en.wikipedia.org/wiki/Blokus
SHAPE_DEFS = (
    ((0, 0),),
    ((0, 0), (1, 0)),
    ((0, 0), (1, 0), (2, 0)),  # 3I
    ((0, 0), (1, 0), (0, 1)),  # 3V
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # 4I
    ((0, 0), (1, 0), (2, 0), (2, 1)),  # 4L
    ((0, 0), (1, 0), (1, 1), (2, 1)),  # 4N
    ((0, 0), (1, 0), (0, 1), (1, 1)),  # 4O
    ((0, 0), (1, 0), (2, 0), (1, 1)),  # 4T
    ((0, 0), (1, 0), (2, 0), (1, 1), (2, -1)),  # 5F
    ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0)),  # 5I
    ((0, 0), (1, 0), (2, 0), (3, 0), (3, 1)),  # 5L
    ((0, 0), (1, 0), (1, 1), (2, 1), (3, 1)),  # 5N
    ((0, 0), (1, 0), (0, 1), (1, 1), (2, 0)),  # 5P
    ((0, 0), (1, 0), (2, 0), (1, 1), (1, 2)),  # 5T
    ((0, 0), (1, 0), (2, 0), (0, 1), (2, 1)),  # 5U
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),  # 5V
    ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2)),  # 5W
    ((0, 0), (1, 0), (2, 0), (1, 1), (1, -1)),  # 5X
    ((0, 0), (1, 0), (2, 0), (2, 1), (3, 0)),  # 5Y
    ((0, 0), (1, 0), (2, 0), (2, 1), (0, -1)),  # 5Z
)


def reformat():
    results = []
    for shape in SHAPE_DEFS:
        with_z = tuple([(x, y, 0) for x, y in shape])
        to_origin = orientation.translated_to_origin(with_z)
        results.append(to_origin)
    return results


def to_pieces(orts):
    pieces = []
    for ort in orts:
        pieces.append(piece.from_orientation(ort))
    return pieces


def get_translations(ort):
    translations = []
    for shift_x in range(BOARD_WIDTH):
        for shift_y in range(BOARD_HEIGHT):
            translated = orientation.translated(ort, shift_x, shift_y, 0)
            if orientation.is_within_bounds(ort, BOARD_WIDTH, 0, BOARD_HEIGHT, 0, 0, 0):
                translations.append(translated)
    return translations


def cube_to_bit(cube):
    bit_number = cube[0] + (cube[1] * BOARD_WIDTH)
    cube_bit = 1 << bit_number
    return cube_bit


def to_occupied_board_bits(ort):
    occupied_bits = 0
    for cube in ort:
        occupied_bits = occupied_bits | cube_to_bit(cube)
    return occupied_bits


def to_orthagonal_board_bits(ort, occupied_bits):
    orthagonal_bits = 0
    for cube in ort:
        x, y, z = cube
        orthagonal_cubes = []
        if x < BOARD_WIDTH:
            orthagonal_cubes.append((x + 1, y))
        if x > 0:
            orthagonal_cubes.append((x - 1, y))
        if y < BOARD_HEIGHT:
            orthagonal_cubes.append((x, y + 1))
        if y > 0:
            orthagonal_cubes.append((x, y - 1))
        for o_cube in orthagonal_cubes:
            orthagonal_bits = orthagonal_bits | cube_to_bit(o_cube)
    not_occupied = ~occupied_bits
    orthagonal_bits = orthagonal_bits & not_occupied
    return orthagonal_bits


def to_diagonal_board_bits(ort, occupied_bits, orthagonal_bits):
    diagonal_bits = 0
    for cube in ort:
        x, y, z = cube
        diagonal_cubes = []
        if x < BOARD_WIDTH and y < BOARD_HEIGHT:
            diagonal_cubes.append((x + 1, y + 1, 0))
        if x > 0 and y < BOARD_HEIGHT:
            diagonal_cubes.append((x - 1, y + 1, 0))
        if x > 0 and y > 0:
            diagonal_cubes.append((x - 1, y - 1, 0))
        if x < BOARD_WIDTH and y > 0:
            diagonal_cubes.append((x + 1, y - 1, 0))
        for d_cube in diagonal_cubes:
            diagonal_bits = diagonal_bits | cube_to_bit(d_cube)
    not_occupied = ~occupied_bits
    not_orthagonal = ~orthagonal_bits
    diagonal_bits = diagonal_bits & not_occupied & not_orthagonal
    return diagonal_bits


def precompute():
    orts = reformat()
    pcs = to_pieces(orts)
    result = {"pieces": {}}
    pc_num = 0
    for pc in pcs:
        pc_num += 1
        result["pieces"][pc_num] = []
        for ort in pc:
            for translation in get_translations(ort):
                occupied = to_occupied_board_bits(translation)
                orthagonal = to_orthagonal_board_bits(translation, occupied)
                diagonal = to_diagonal_board_bits(translation, occupied, orthagonal)
                board_bits = {
                    "occupied": occupied,
                    "orthagonal": orthagonal,
                    "diagonal": diagonal,
                }
                result["pieces"][pc_num].append(board_bits)

    with open("blokus.json", "w") as f:
        j = json.dumps(result, indent=4)
        print(j, file=f)


def print_bits(board_bits):
    bin_str = "{0:0400b}".format(board_bits)[::-1]
    header = "    12345  67890  12345  67890"
    print(header)
    for row in range(BOARD_HEIGHT, 0, -1):
        if row % 5 == 0:
            print(" ")
        line_start = (row - 1) * BOARD_WIDTH
        line_end = line_start + BOARD_WIDTH
        line = bin_str[line_start:line_end]
        spaced = "  ".join([line[i : i + 5] for i in range(0, len(line), 5)])
        print(f"{row:02}  {spaced}")
    print(" ")
    print(header)


if __name__ == "__main__":
    # precompute()
