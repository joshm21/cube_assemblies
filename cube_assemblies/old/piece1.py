from cube import Cube
import transform as Transform


class Piece:
    """An immutable, equatable, physical piece represented by a set of cubes in a right hand, 3D coordinate systme"""

    def __init__(self, set_of_cubes):
        self.cubes = self.create_frozen_set(set_of_cubes)

    @staticmethod
    def create_frozen_set(cubes):
        frozen_cube_set = frozenset(cubes)
        if len(frozen_cube_set) is not len(cubes):
            raise TypeError('Cannot pass set with duplicate cubes.')
        for cube in frozen_cube_set:
            if not isinstance(cube, Cube):
                raise TypeError('Expected Cube instances.')
        return frozen_cube_set

    def __repr__(self):
        cubes_string = ','.join((cube.__repr__() for cube in self.cubes))
        return f'Piece(({cubes_string}))'

    def __str__(self):
        cubes_string = ','.join((cube.__str__() for cube in self.cubes))
        return f'Piece({cubes_string})'

    def __eq__(self):
        """Two pieces are equal if they represent the same physical piece.
        i.e. they can be rotated to match each other and have the same 24 orientations"""
        pass
