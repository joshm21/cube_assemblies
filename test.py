import unittest
from cube import Cube
from orientation import Orientation
from piece import Piece
from generate import generate_polyominos, generate_polycubes, generate_six_piece_burr


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

    def test_get_rotatation(self):
        self.assertTrue(Cube(1, 2, 3).get_rotated("x") == Cube(1, -3, 2))
        self.assertTrue(Cube(2, 3, -4).get_rotated("x") == Cube(2, 4, 3))
        self.assertTrue(Cube(3, -4, 5).get_rotated("x") == Cube(3, -5, -4))
        self.assertTrue(Cube(4, -5, -6).get_rotated("x") == Cube(4, 6, -5))
        self.assertTrue(Cube(-5, 6, 7).get_rotated("x") == Cube(-5, -7, 6))
        self.assertTrue(Cube(-6, 7, -8).get_rotated("x") == Cube(-6, 8, 7))
        self.assertTrue(Cube(-7, -8, 9).get_rotated("x") == Cube(-7, -9, -8))
        self.assertTrue(Cube(-8, -9, -10).get_rotated("x") == Cube(-8, 10, -9))
        self.assertTrue(Cube(1, 2, 3).get_rotated("y") == Cube(3, 2, -1.0))
        self.assertTrue(Cube(2, 3, -4).get_rotated("y") == Cube(-4, 3, -2))
        self.assertTrue(Cube(3, -4, 5).get_rotated("y") == Cube(5, -4, -3))
        self.assertTrue(Cube(4, -5, -6).get_rotated("y") == Cube(-6, -5, -4))
        self.assertTrue(Cube(-5, 6, 7).get_rotated("y") == Cube(7, 6, 5))
        self.assertTrue(Cube(-6, 7, -8).get_rotated("y") == Cube(-8, 7, 6))
        self.assertTrue(Cube(-7, -8, 9).get_rotated("y") == Cube(9, -8, 7))
        self.assertTrue(Cube(-8, -9, -10).get_rotated("y") == Cube(-10, -9, 8))
        self.assertTrue(Cube(1, 2, 3).get_rotated("z") == Cube(-2, 1, 3))
        self.assertTrue(Cube(2, 3, -4).get_rotated("z") == Cube(-3, 2, -4))
        self.assertTrue(Cube(3, -4, 5).get_rotated("z") == Cube(4, 3, 5))
        self.assertTrue(Cube(4, -5, -6).get_rotated("z") == Cube(5, 4, -6))
        self.assertTrue(Cube(-5, 6, 7).get_rotated("z") == Cube(-6, -5, 7))
        self.assertTrue(Cube(-6, 7, -8).get_rotated("z") == Cube(-7, -6, -8))
        self.assertTrue(Cube(-7, -8, 9).get_rotated("z") == Cube(8, -7, 9))
        self.assertTrue(Cube(-8, -9, -10).get_rotated("z") == Cube(9, -8, -10))


class TestOrientation(unittest.TestCase):
    def test_init_duplicates(self):
        with self.assertRaises(ValueError):
            Orientation.from_xyzs(((1, 2, 3), (1, 2, 3)))

    def test_from_xyzs(self):
        self.assertEqual(
            Orientation((Cube(1, 2, 3), Cube(4, 5, 6))),
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))),
        )

    def test_equality(self):
        self.assertEqual(
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))),
        )
        self.assertEqual(
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyzs(((4, 5, 6), (1, 2, 3))),
        )
        self.assertNotEqual(
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))),
            Orientation.from_xyzs(((9, 9, 9), (8, 8, 8))),
        )

    def test_immutable_cubes_attribute(self):
        with self.assertRaises(Exception):
            test_orientation = Orientation.from_xyzs(((1, 2, 3), (4, 5, 6)))
            test_orientation.cubes = 1

    def test_immutable_individual_cubes(self):
        with self.assertRaises(Exception):
            test_orientation = Orientation.from_xyzs(((1, 2, 3), (4, 5, 6)))
            test_orientation.cubes[0] = Cube(1, 2, 3)

    def test_str(self):
        self.assertEqual(
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))).__str__(), "((1,2,3),(4,5,6))"
        )

    def test_sorted_cubes(self):
        self.assertEqual(
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))).__str__(),
            Orientation.from_xyzs(((4, 5, 6), (1, 2, 3))).__str__(),
        )

    def test_get_rotated(self):
        self.assertEqual(
            Orientation.from_xyzs(((1, 2, 3), (2, 3, -4))).get_rotated("x"),
            Orientation.from_xyzs(((1, -3, 2), (2, 4, 3))),
        )

    def test_get_translated_to_origin(self):
        self.assertEqual(
            Orientation.from_xyzs(((-1, -2, -3), (4, 5, 6))).get_translated_to_origin(),
            Orientation.from_xyzs(((0, 0, 0), (5, 7, 9))),
        )
        self.assertEqual(
            Orientation.from_xyzs(((1, 2, 3), (4, 5, 6))).get_translated_to_origin(),
            Orientation.from_xyzs(((0, 0, 0), (3, 3, 3))),
        )


class TestPiece(unittest.TestCase):
    def test_from_xyzs(self):
        self.assertEqual(
            Piece(Orientation((Cube(1, 2, 3), Cube(4, 5, 6)))),
            Piece.from_xyzs(((1, 2, 3), (4, 5, 6))),
        )

    def test_get_unique_orientations(self):
        self.assertEqual(
            Piece.from_xyzs(((0, 0, 0), (0, 0, 1))).orientations,
            frozenset(
                (
                    Orientation.from_xyzs(((0, 0, 0), (0, 0, 1))),
                    Orientation.from_xyzs(((0, 0, 0), (0, 1, 0))),
                    Orientation.from_xyzs(((0, 0, 0), (1, 0, 0))),
                )
            ),
        )

        # test that orientations always the same, no matter which orientation used to init Piece
        orts = Piece.from_xyzs(
            ((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0))
        ).orientations
        for ort in orts:
            self.assertEqual(Piece(ort).orientations, orts)

        self.assertEqual(
            Piece.from_xyzs(((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0))),
            Piece.from_xyzs(((2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0))),
        )

    def test_equality(self):
        self.assertEqual(
            Piece.from_xyzs(((0, 0, 0), (0, 0, 1))),
            Piece.from_xyzs(((0, 0, 0), (1, 0, 0))),
        )
        self.assertNotEqual(
            Piece.from_xyzs(((0, 0, 0), (0, 0, 1))),
            Piece.from_xyzs(((0, 0, 0), (0, 0, 2))),
        )
        self.assertEqual(
            Piece.from_xyzs(((2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0))),
            Piece.from_xyzs(((0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0))),
        )

        # ensure equal if not initialized at origin
        self.assertEqual(
            Piece.from_xyzs(((0, 0, 0), (1, 0, 0))),
            Piece.from_xyzs(((8, 2, 4), (9, 2, 4))),
        )

    def test_set_operations(self):
        piece1 = Piece.from_xyzs(((0, 0, 0), (1, 0, 0)))
        piece2 = Piece.from_xyzs(((1, 0, 0), (0, 0, 0)))  # same as piece1
        piece3 = Piece.from_xyzs(((9, 9, 9), (8, 8, 8)))  # different
        self.assertEqual(len(set([piece1, piece2])), 1)
        self.assertEqual(len(set([piece1, piece2, piece3])), 2)


class TestGenerate(unittest.TestCase):
    def test_generate_polyomino(self):
        self.assertEqual(len(generate_polyominos(5)), 21)

    def test_generate_polycube(self):
        self.assertEqual(len(generate_polycubes(4)), 12)


if __name__ == "__main__":
    unittest.main()
