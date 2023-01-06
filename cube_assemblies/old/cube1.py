class Cube:
    """A unit cube in a right hand, 3D coordinate system

    z   y
    |  /
    | /
    +---- x
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Cube({self.x},{self.y},{self.z})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        # https://stackoverflow.com/a/1227325/10568900
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.x, self.y, self.z))

    def translate_x(self, x):
        self.x += x
        return self

    def translate_y(self, y):
        self.y += y
        return self

    def translate_z(self, z):
        self.z += z
        return self

    def rotate_x(self):
        new_y = -1 * self.z
        new_z = self.y
        self.y = new_y
        self.z = new_z
        return self

    def rotate_y(self):
        new_x = self.z
        new_z = -1 * self.x
        self.x = new_x
        self.z = new_z
        return self

    def rotate_z(self):
        new_x = -1 * self.y
        new_y = self.x
        self.x = new_x
        self.y = new_y
        return self


# tests

# def test_translate_x(self):
#         self.assertTrue(Cube(1, 2, 3).translate_x(12) == Cube(13, 2, 3))
#         self.assertTrue(Cube(1, 2, 3).translate_x(-12) == Cube(-11, 2, 3))

#     def test_translate_y(self):
#         self.assertTrue(Cube(1, 2, 3).translate_y(12) == Cube(1, 14, 3))
#         self.assertTrue(Cube(1, 2, 3).translate_y(-12) == Cube(1, -10, 3))

#     def test_translate_z(self):
#         self.assertTrue(Cube(1, 2, 3).translate_z(12) == Cube(1, 2, 15))
#         self.assertTrue(Cube(1, 2, 3).translate_z(-12) == Cube(1, 2, -9))

#     def test_rotate_x(self):
#         self.assertTrue(Cube(1, 2, 3).rotate_x() == Cube(1, -3, 2))
#         self.assertTrue(Cube(2, 3, -4).rotate_x() == Cube(2, 4, 3))
#         self.assertTrue(Cube(3, -4, 5).rotate_x() == Cube(3, -5, -4))
#         self.assertTrue(Cube(4, -5, -6).rotate_x() == Cube(4, 6, -5))
#         self.assertTrue(Cube(-5, 6, 7).rotate_x() == Cube(-5, -7, 6))
#         self.assertTrue(Cube(-6, 7, -8).rotate_x() == Cube(-6, 8, 7))
#         self.assertTrue(Cube(-7, -8, 9).rotate_x() == Cube(-7, -9, -8))
#         self.assertTrue(Cube(-8, -9, -10).rotate_x() == Cube(-8, 10, -9))

#     def test_rotate_y(self):
#         self.assertTrue(Cube(1, 2, 3).rotate_y() == Cube(3, 2, -1.))
#         self.assertTrue(Cube(2, 3, -4).rotate_y() == Cube(-4, 3, -2))
#         self.assertTrue(Cube(3, -4, 5).rotate_y() == Cube(5, -4, -3))
#         self.assertTrue(Cube(4, -5, -6).rotate_y() == Cube(-6, -5, -4))
#         self.assertTrue(Cube(-5, 6, 7).rotate_y() == Cube(7, 6, 5))
#         self.assertTrue(Cube(-6, 7, -8).rotate_y() == Cube(-8, 7, 6))
#         self.assertTrue(Cube(-7, -8, 9).rotate_y() == Cube(9, -8, 7))
#         self.assertTrue(Cube(-8, -9, -10).rotate_y() == Cube(-10, -9, 8))

#     def test_rotate_z(self):
#         self.assertTrue(Cube(1, 2, 3).rotate_z() == Cube(-2, 1, 3))
#         self.assertTrue(Cube(2, 3, -4).rotate_z() == Cube(-3, 2, -4))
#         self.assertTrue(Cube(3, -4, 5).rotate_z() == Cube(4, 3, 5))
#         self.assertTrue(Cube(4, -5, -6).rotate_z() == Cube(5, 4, -6))
#         self.assertTrue(Cube(-5, 6, 7).rotate_z() == Cube(-6, -5, 7))
#         self.assertTrue(Cube(-6, 7, -8).rotate_z() == Cube(-7, -6, -8))
#         self.assertTrue(Cube(-7, -8, 9).rotate_z() == Cube(8, -7, 9))
#         self.assertTrue(Cube(-8, -9, -10).rotate_z() == Cube(9, -8, -10))
