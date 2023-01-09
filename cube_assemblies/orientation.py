from cube import Cube
from dataclasses import dataclass


@dataclass(frozen=True)
class Orientation:
    cubes: tuple[Cube]

    def __init__(self, cubes: tuple[Cube]) -> 'Orientation':
        object.__setattr__(self, 'cubes',
                           tuple((cube for cube in sorted(cubes))))
        self.check_for_duplicates()

    @classmethod
    def from_xyz(cls, xyz_tuples: tuple[tuple]) -> 'Orientation':
        return cls(tuple((Cube(*xyz) for xyz in xyz_tuples)))

    def __str__(self) -> str:
        return f'({",".join((cube.__str__() for cube in self.cubes))})'

    def check_for_duplicates(self) -> None:
        if len(self.cubes) != len(set(self.cubes)):
            raise ValueError('Orientation cannot contain duplicate cubes')

    def rotate(self, axis: str) -> 'Orientation':
        """Returns a new orientation rotated 90 degrees counterclockwise about axis in right hand coordinate system"""
        return Orientation((cube.rotate(axis) for cube in self.cubes))

    def translate_to_origin(self) -> 'Orientation':
        """Returns a new orientation translated as close to origin as possible with x,y,z >= 0"""
        x_min = min((cube.x for cube in self.cubes))
        y_min = min((cube.y for cube in self.cubes))
        z_min = min((cube.z for cube in self.cubes))
        return Orientation((cube.translate(-1 * x_min, -1 * y_min, -1 * z_min) for cube in self.cubes))

    def has_cube(self, cube: Cube) -> bool:
        return cube in self.cubes

    def add_cube(self, cube: Cube) -> 'Orientation':
        return Orientation((*self.cubes, cube))
