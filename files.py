def save_orientations(filename: str, orientations: list) -> None:
    with open(filename, "w") as f:
        for ort in sorted(orientations):
            f.write(str(sorted(ort)))
            f.write("\n")


def save_pieces(filename: str, pieces: list) -> None:
    with open(filename, "w") as f:
        for piece in pieces:
            f.write("[")
            for ort in piece:
                f.write(str(sorted(ort)))
                f.write(", ")
            f.write("]")
            f.write("\n")
