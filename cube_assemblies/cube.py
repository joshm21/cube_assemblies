from dataclasses import dataclass


@dataclass(frozen=True)
class Cube:
    x: int
    y: int
    z: int

    def rotate(self, axis: str) -> 'Cube':
        """Returns a new cube rotated 90 degrees counterclockwise about axis in right hand coordinate system"""
        if axis == 'x':
            return Cube(self.x, -1 * self.z, self.y)
        if axis == 'y':
            return Cube(self.z, self.y, -1 * self.x)
        if axis == 'z':
            return Cube(-1 * self.y, self.x, self.z)
        raise ValueError(f'Rotation axis must be x, y, or z, not {axis}')

    def translate(self, x: int, y: int, z: int) -> 'Cube':
        """Returns a new cube translated by x,y,z amounts"""
        return Cube(self.x + x, self.y + y, self.z + z)
