from orientation import Orientation
from dataclasses import dataclass


@dataclass(frozen=True)
class Piece:
    initial_orientation: Orientation
    orientations: frozenset[Orientation]

    def __init__(self, orientation: Orientation) -> 'Piece':
        object.__setattr__(self, 'initial_orientation', orientation)
        object.__setattr__(self, 'orientations',
                           Piece.get_orientations_set(orientation))

    @classmethod
    def from_xyz(cls, xyz_tuples: tuple[tuple]) -> 'Piece':
        return cls(Orientation.from_xyz(xyz_tuples))

    def __str__(self):
        return f'Piece with {len(self.orientations)} unique orientations. One orientation below:\n{self.initial_orientation.__str__()}'

    def __eq__(self, other):
        return self.orientations == other.orientations

    @staticmethod
    def get_orientations_set(orientation: Orientation) -> frozenset[Orientation]:
        """Returns all unique orientations of 1 physical piece (max of 24 orientations)
        All orientations are translated as close to origin as possible with  x,y,z >= 0"""
        top_face_up = orientation
        top_face_forward = orientation.rotate('x').translate_to_origin()
        top_face_down = top_face_forward.rotate('x').translate_to_origin()
        top_face_back = top_face_down.rotate('x').translate_to_origin()
        top_face_right = top_face_up.rotate('y').translate_to_origin()
        top_face_left = top_face_down.rotate('y').translate_to_origin()
        top_face_directions = [top_face_up, top_face_forward,
                               top_face_down, top_face_back, top_face_right, top_face_left]
        orientations = []
        for top_face_direction in top_face_directions:
            orientations.append(top_face_direction)
            for _ in range(3):
                last_orientation = orientations[-1]
                rotated = last_orientation.rotate('z').translate_to_origin()
                orientations.append(rotated)
        return frozenset(orientations)


if __name__ == '__main__':
    print(Piece.from_xyz(((0, 0, 0), (0, 0, 1))))
