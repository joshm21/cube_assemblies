from cube import Cube
from dataclasses import dataclass


@dataclass(frozen=True)
class Piece:
    cubes: frozenset[Cube]

    def __post_init__(self) -> None:
        if not isinstance(self.cubes, frozenset):
            raise TypeError('Expected a frozenset of Cubes')
        for cube in self.cubes:
            if not isinstance(cube, Cube):
                raise TypeError('Expects Cube instances')

    @classmethod
    def from_xyz(cls, tuples) -> 'Piece':
        return Piece(frozenset([Cube(*tuple) for tuple in tuples]))

    def rotate(self, axis: str) -> 'Piece':
        """Returns a new piece rotated 90 degrees counterclockwise about axis in right hand coordinate system"""
        return Piece(frozenset([cube.rotate(axis) for cube in self.cubes]))

    def translate_to_origin(self) -> 'Piece':
        """Returns a new piece translated as close to origin as possible with x,y,z >= 0"""
        x_min = min((cube.x for cube in self.cubes))
        y_min = min((cube.y for cube in self.cubes))
        z_min = min((cube.z for cube in self.cubes))
        return Piece(frozenset([cube.translate(-1 * x_min, -1 * y_min, -1 * z_min) for cube in self.cubes]))

    def get_24_positive_orientations(self) -> tuple['Piece']:
        """Returns a tuple of of 24 orientations of 1 physical piece.
        All orientations are translated as close to origin as possible with  x,y,z >= 0"""
        top_face_up = self
        top_face_forward = self.rotate('x').translate_to_origin()
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
        return tuple(orientations)
