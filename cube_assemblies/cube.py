from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Cube:
    x: int
    y: int
    z: int

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

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

    def get_neighbors(self, x_max: int, y_max: int, z_max: int) -> tuple['Cube']:
        neighbors = []
        if self.x < x_max:
            neighbors.append(Cube(self.x + 1, self.y, self.z))
        if self.x > 0:
            neighbors.append(Cube(self.x - 1, self.y, self.z))
        if self.y < y_max:
            neighbors.append(Cube(self.x, self.y + 1, self.z))
        if self.y > 0:
            neighbors.append(Cube(self.x, self.y - 1, self.z))
        if self.z < z_max:
            neighbors.append(Cube(self.x, self.y, self.z + 1))
        if self.z > 0:
            neighbors.append(Cube(self.x, self.y, self.z - 1))
        return tuple(neighbors)
