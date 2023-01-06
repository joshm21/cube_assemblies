from dataclasses import dataclass


@dataclass(frozen=True)
class Cube:
    """An immutable, equatable unit cube in a right hand, 3D coordinate system

    z   y
    |  /
    | /
    +---- x
    """

    x: int
    y: int
    z: int

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
