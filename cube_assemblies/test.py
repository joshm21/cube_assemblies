import unittest
from cube import Cube
from orientation import Orientation
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

    def test_get_neighbors(self):
        neighbors = Cube(1, 1, 1).get_neighbors()
        self.assertIn(Cube(2, 1, 1), neighbors)
        self.assertIn(Cube(0, 1, 1), neighbors)
        self.assertIn(Cube(1, 2, 1), neighbors)
        self.assertIn(Cube(1, 0, 1), neighbors)
        self.assertIn(Cube(1, 1, 2), neighbors)
        self.assertIn(Cube(1, 1, 0), neighbors)


class TestOrientation(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))).__str__(),
            '((1,2,3),(4,5,6))')

    def test_equality(self):
        self.assertEqual(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))))
        self.assertNotEqual(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyz(((9, 9, 9), (8, 8, 8))))

    def test_init_sorting(self):
        self.assertEqual(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyz(((4, 5, 6), (1, 2, 3))))

    def test_init_duplicates(self):
        with self.assertRaises(ValueError):
            Orientation.from_xyz(((1, 2, 3), (1, 2, 3)))

    def test_from_xyz(self):
        self.assertEqual(
            Orientation((Cube(1, 2, 3), Cube(4, 5, 6))),
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))))

    def test_immutable_cubes_attribute(self):
        with self.assertRaises(Exception):
            test_orientation = Orientation.from_xyz(((1, 2, 3), (4, 5, 6)))
            test_orientation.cubes = 1

    def test_immutable_individual_cubes(self):
        with self.assertRaises(Exception):
            test_orientation = Orientation.from_xyz(((1, 2, 3), (4, 5, 6)))
            test_orientation.cubes[0] = Cube(1, 2, 3)

    def test_rotate(self):
        self.assertEqual(
            Orientation.from_xyz(((1, 2, 3), (2, 3, -4))).rotate('x'),
            Orientation.from_xyz(((1, -3, 2), (2, 4, 3))))

    def test_translate_to_origin(self):
        self.assertEqual(
            Orientation.from_xyz(((-1, -2, -3), (4, 5, 6))
                                 ).translate_to_origin(),
            Orientation.from_xyz(((0, 0, 0), (5, 7, 9))))
        self.assertEqual(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))).translate_to_origin(),
            Orientation.from_xyz(((0, 0, 0), (3, 3, 3))))

    def test_has_cube(self):
        self.assertTrue(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))
                                 ).has_cube(Cube(1, 2, 3)))
        self.assertFalse(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))
                                 ).has_cube(Cube(9, 9, 9)))

    def test_add_cube(self):
        self.assertEqual(
            Orientation.from_xyz(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyz(((1, 2, 3),)).add_cube(Cube(4, 5, 6))
        )


class TestPiece(unittest.TestCase):

    def test_from_xyz(self):
        self.assertEqual(
            Piece(Orientation((Cube(1, 2, 3), Cube(4, 5, 6)))),
            Piece.from_xyz(((1, 2, 3), (4, 5, 6))))

    def test_get_unique_orientations(self):
        self.assertEqual(
            Piece.from_xyz(((0, 0, 0), (0, 0, 1))).orientations,
            frozenset((
                Orientation.from_xyz(((0, 0, 0), (0, 0, 1))),
                Orientation.from_xyz(((0, 0, 0), (0, 1, 0))),
                Orientation.from_xyz(((0, 0, 0), (1, 0, 0)))
            ))
        )

    def test_equality(self):
        self.assertEqual(
            Piece.from_xyz(((0, 0, 0), (0, 0, 1))),
            Piece.from_xyz(((0, 0, 0), (1, 0, 0)))
        )
        self.assertNotEqual(
            Piece.from_xyz(((0, 0, 0), (0, 0, 1))),
            Piece.from_xyz(((0, 0, 0), (0, 0, 2)))
        )


if __name__ == '__main__':
    unittest.main()
