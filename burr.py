from . import orientation as Orientation
from .generate import generate_by_combos, to_unique_pieces
from . import cutler as Cutler


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


def prep_for_assemblies():
    pass


def test():
    # https://billcutlerpuzzles.com/docs/CA6PB/pieces.html
    print("Testing six piece burrs...")

    all_mine = frozenset(generate_six_piece_burr_orientations())
    all_his = {
        Cutler.to_orientation(cutler_string) for cutler_string in Cutler.ALL_STRINGS
    }
    print(f"Orientations match? {all_mine == all_his}")

    notchable_mine = {ort for ort in all_mine if Orientation.is_notchable(ort)}
    notchable_his = {
        Cutler.to_orientation(cutler_string)
        for cutler_string in Cutler.NOTCHABLE_STRINGS
    }
    print(f"Notchable orientations match? {notchable_mine == notchable_his}")

    pieces_mine = len(to_unique_pieces(all_mine))
    pieces_his = 837
    print(f"Pieces match? {pieces_mine == pieces_his}")

    notchable_pieces_mine = len(to_unique_pieces(notchable_mine))
    notchable_pieces_his = 59
    print(f"Notchable pieces match? {notchable_pieces_mine == notchable_pieces_his}")


def main():
    test()


if __name__ == "__main__":
    main()
