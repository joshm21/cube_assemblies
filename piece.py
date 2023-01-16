from dataclasses import dataclass
from orientation import Orientation


@dataclass(frozen=True)
class Piece:
    orientations: frozenset[Orientation]

    def __init__(self, orientation: Orientation) -> 'Piece':
        object.__setattr__(self, 'orientations',
                           Piece.get_orientations_set(orientation))

    @classmethod
    def from_xyzs(cls, tuple_of_xyz_tuples: tuple[tuple[int, int, int]]) -> 'Piece':
        return cls(Orientation.from_xyzs(tuple_of_xyz_tuples))

    def __str__(self) -> str:
        return [ort.__str__() for ort in self.orientations].sort()[0]

    @staticmethod
    def get_orientations_set(orientation: Orientation) -> frozenset[Orientation]:
        """Returns all unique orientations of 1 physical piece (max of 48 orientations)
        All orientations are translated as close to origin as possible with  x,y,z >= 0

        Point top face in each direction and rotate 4 total times for 24 orientations
        then take original orientation, reflect (rotate twice) and repeat process for 48 total"""

        def get_top_face_each_direction(orientation: Orientation) -> list[Orientation]:
            up = orientation.get_translated_to_origin()
            forward = up.get_rotated('x').get_translated_to_origin()
            down = forward.get_rotated('x').get_translated_to_origin()
            back = down.get_rotated('x').get_translated_to_origin()
            right = up.get_rotated('y').get_translated_to_origin()
            left = down.get_rotated('y').get_translated_to_origin()
            return [up, forward, down, back, right, left]

        top_face_directions = get_top_face_each_direction(orientation)
        mirrored_xy = orientation.get_rotated(
            'z').get_rotated('z').get_translated_to_origin()
        mirrored_top_face_directions = get_top_face_each_direction(mirrored_xy)
        all_top_face_directions = top_face_directions + mirrored_top_face_directions

        orientations = []
        for top_face_direction in all_top_face_directions:
            orientations.append(top_face_direction)
            for _ in range(3):
                last_orientation = orientations[-1]
                rotated = last_orientation.get_rotated(
                    'z').get_translated_to_origin()
                orientations.append(rotated)
        return frozenset(orientations)
