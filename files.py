def save_orientations(filename: str, orientations: list) -> None:
    with open(filename, "w") as f:
        for ort in sorted(orientations):
            f.write(str(sorted(ort)))
            f.write("\n")


def save_pieces(filename: str, pieces: list) -> None:
    orientations = [sorted(piece)[0] for piece in sorted(pieces)]
    save_orientations(filename, orientations)
