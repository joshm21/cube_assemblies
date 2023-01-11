from cube import Cube
import plot as plot
from dataclasses import dataclass


@dataclass(frozen=True)
class Orientation:
    cubes: frozenset[Cube]

    def __init__(self, cubes: tuple[Cube]) -> 'Orientation':
        object.__setattr__(self, 'cubes', frozenset(cubes))
        self.check_for_duplicates(cubes)

    def check_for_duplicates(self, cubes) -> None:
        if len(cubes) != len(self.cubes):
            raise ValueError('Orientation cannot contain duplicate cubes')

    @ classmethod
    def from_xyz(cls, xyz_tuples: tuple[tuple]) -> 'Orientation':
        return cls(tuple((Cube(*xyz) for xyz in xyz_tuples)))

    @ property
    def center_of_mass(self) -> tuple[int]:
        x_total = 0
        y_total = 0
        z_total = 0
        for cube in self.cubes:
            x_total += cube.x
            y_total += cube.y
            z_total += cube.z
        number_cubes = len(self.cubes)
        return (x_total / number_cubes, y_total / number_cubes, z_total / number_cubes)

    def __str__(self) -> str:
        return f'({",".join((cube.__str__() for cube in self.get_sorted_cubes()))})'

    def __eq__(self, other) -> bool:
        return set(self.cubes) == set(other.cubes)

    def get_sorted_cubes(self) -> tuple[Cube]:
        """Sort ascending by z, then y, then x"""
        return sorted(self.cubes, key=lambda cube: (cube.z, cube.y, cube.x))

    def get_rotated(self, axis: str) -> 'Orientation':
        """Returns a new orientation rotated 90 degrees counterclockwise about axis in right hand coordinate system"""
        return Orientation(tuple(cube.get_rotated(axis) for cube in self.cubes))

    def get_translated_to_origin(self) -> 'Orientation':
        """Returns a new orientation translated as close to origin as possible with x,y,z >= 0"""
        x_min = min((cube.x for cube in self.cubes))
        y_min = min((cube.y for cube in self.cubes))
        z_min = min((cube.z for cube in self.cubes))
        return Orientation(tuple(cube.get_translated(-1 * x_min, -1 * y_min, -1 * z_min) for cube in self.cubes))

    def plot(self) -> None:
        points = []
        for cube in self.cubes:
            points.append((cube.x, cube.y, cube.z))
        plot.plot(points)


if __name__ == '__main__':
    Orientation.from_xyz(((0, 0, 0), (0, 0, 1))).plot()
