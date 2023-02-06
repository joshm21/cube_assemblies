from . import orientation as Orientation

Piece = frozenset[Orientation.Orientation]


def from_orientation(orientation: Orientation.Orientation) -> Piece:
    """Given an orientation representing a physical piece, get all unique orientations of that piece in 3D space
    All orientations are translated as close to the origin as possible with x,y,z >= 0
    Max of 24 orientations: top face pointed in each direction and rotated four times"""

    rX = Orientation.rotated_x
    rY = Orientation.rotated_y
    rZ = Orientation.rotated_z

    up = orientation
    front = rX(up)
    down = rX(front)
    back = rX(down)
    right = rY(up)
    left = rY(rY(rY(up)))

    top_face_directions = (up, front, down, back, right, left)

    all_orientations = []
    for top_face_direction in top_face_directions:
        all_orientations.append(Orientation.translated_to_origin(top_face_direction))
        for _ in range(3):
            previous_orientation = all_orientations[-1]
            rotated_z = Orientation.rotated_z(previous_orientation)
            all_orientations.append(Orientation.translated_to_origin(rotated_z))
    return frozenset(all_orientations)
