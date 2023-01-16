from orientation import Orientation
from piece import Piece


def save_pieces(pieces: list[Piece], filename: str) -> None:
    __save_list_of_stringables(pieces, filename)


def save_orientations(orientations: list[Orientation], filename: str) -> None:
    __save_list_of_stringables(orientations, filename)


def __save_list_of_stringables(stringables: list, filename: str) -> None:
    with open(filename, 'w') as f:
        for stringable in stringables:
            f.write(stringable.__str__())
            f.write('\n')


def load_pieces(filename: str) -> list[Piece]:
    pieces = []
    for xyzs in __load_xyzs(filename):
        pieces.append(Piece.from_xyzs(xyzs))
    return pieces


def load_orientations(filename: str) -> list[Orientation]:
    orientations = []
    for xyzs in __load_xyzs(filename):
        orientations.append(Orientation.from_xyzs(xyzs))
    return orientations


def __load_xyzs(filename: str) -> list[tuple[int]]:
    xyzs = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            xyzs.append(eval(line))
    return xyzs
