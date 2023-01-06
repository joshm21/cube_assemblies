import unittest
from cube import Cube
from piece import Piece


class TestCube(unittest.TestCase):

    def test_xyz_attributes(self):
        test_cube = Cube(1, 2, 3)
        self.assertEqual(test_cube.x, 1)
        self.assertEqual(test_cube.y, 2)
        self.assertEqual(test_cube.z, 3)

    def test_immutability(self):
        with self.assertRaises(Exception):
            Cube(1, 2, 3).x = 9

    def test_equality(self):
        self.assertTrue(Cube(1, 2, 3) == Cube(1, 2, 3))
        self.assertFalse(Cube(1, 2, 3) == Cube(9, 9, 9))

    def test_rotate(self):
        self.assertTrue(Cube(1, 2, 3).rotate('x') == Cube(1, -3, 2))
        self.assertTrue(Cube(2, 3, -4).rotate('x') == Cube(2, 4, 3))
        self.assertTrue(Cube(3, -4, 5).rotate('x') == Cube(3, -5, -4))
        self.assertTrue(Cube(4, -5, -6).rotate('x') == Cube(4, 6, -5))
        self.assertTrue(Cube(-5, 6, 7).rotate('x') == Cube(-5, -7, 6))
        self.assertTrue(Cube(-6, 7, -8).rotate('x') == Cube(-6, 8, 7))
        self.assertTrue(Cube(-7, -8, 9).rotate('x') == Cube(-7, -9, -8))
        self.assertTrue(Cube(-8, -9, -10).rotate('x') == Cube(-8, 10, -9))
        self.assertTrue(Cube(1, 2, 3).rotate('y') == Cube(3, 2, -1.))
        self.assertTrue(Cube(2, 3, -4).rotate('y') == Cube(-4, 3, -2))
        self.assertTrue(Cube(3, -4, 5).rotate('y') == Cube(5, -4, -3))
        self.assertTrue(Cube(4, -5, -6).rotate('y') == Cube(-6, -5, -4))
        self.assertTrue(Cube(-5, 6, 7).rotate('y') == Cube(7, 6, 5))
        self.assertTrue(Cube(-6, 7, -8).rotate('y') == Cube(-8, 7, 6))
        self.assertTrue(Cube(-7, -8, 9).rotate('y') == Cube(9, -8, 7))
        self.assertTrue(Cube(-8, -9, -10).rotate('y') == Cube(-10, -9, 8))
        self.assertTrue(Cube(1, 2, 3).rotate('z') == Cube(-2, 1, 3))
        self.assertTrue(Cube(2, 3, -4).rotate('z') == Cube(-3, 2, -4))
        self.assertTrue(Cube(3, -4, 5).rotate('z') == Cube(4, 3, 5))
        self.assertTrue(Cube(4, -5, -6).rotate('z') == Cube(5, 4, -6))
        self.assertTrue(Cube(-5, 6, 7).rotate('z') == Cube(-6, -5, 7))
        self.assertTrue(Cube(-6, 7, -8).rotate('z') == Cube(-7, -6, -8))
        self.assertTrue(Cube(-7, -8, 9).rotate('z') == Cube(8, -7, 9))
        self.assertTrue(Cube(-8, -9, -10).rotate('z') == Cube(9, -8, -10))


class TestPiece(unittest.TestCase):

    def test_from_xyz_tuples(self):
        self.assertEqual(Piece(frozenset([Cube(1, 2, 3), Cube(4, 5, 6)])),
                         Piece.from_xyz([(1, 2, 3), (4, 5, 6)]))

    def test_immutable_cubes_attribute(self):
        with self.assertRaises(Exception):
            test_piece = Piece.from_xyz([(1, 2, 3), (4, 5, 6)])
            test_piece.cubes = 1

    def test_immutable_individual_cubes(self):
        with self.assertRaises(Exception):
            test_piece = Piece.from_xyz([(1, 2, 3), (4, 5, 6)])
            test_piece.cubes[0] = Cube(1, 2, 3)

    def test_equality(self):
        self.assertTrue(
            Piece.from_xyz([(1, 2, 3), (4, 5, 6)]),
            Piece.from_xyz([(1, 2, 3), (4, 5, 6)]))

    def test_rotate(self):
        self.assertTrue(
            Piece.from_xyz([(1, 2, 3), (2, 3, -4)]),
            Piece.from_xyz([(1, -3, 2), (2, 3, 4)]))

    def test_translate_to_origin(self):
        self.assertTrue(
            Piece.from_xyz([(-1, -2, -3), (4, 5, 6)]),
            Piece.from_xyz([(0, 0, 0), (5, 7, 9)]))
        self.assertTrue(
            Piece.from_xyz([(1, 2, 3), (4, 5, 6)]),
            Piece.from_xyz([(0, 0, 0), (3, 3, 3)]))

    def test_get_24_positive_orientations(self):
        orientations = Piece.from_xyz(
            [(1, 2, 3)]).get_24_positive_orientations()
        self.assertIn(Piece.from_xyz([(1, 2, 3)]), orientations)
        # TODO fill this out
