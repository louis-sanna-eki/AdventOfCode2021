
import unittest
from solve import find_neighbors

HALLWAY_LENGTH = 11
ROOM_COUNT = 4
FREE_SPOT_COUNT = 11 - 4


class TestSolve(unittest.TestCase):

    def test_trivial_case(self):
        neighbors = find_neighbors(
            (".") * HALLWAY_LENGTH, (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors, [])

    def test_one_step_from_victory(self):
        neighbors = find_neighbors(("A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."), (
            ("A", "."), ("B", "B"), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors[0][0], (".", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."))
        self.assertEqual(neighbors[0][1], (("A", "A"), (
            "B", "B"), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors[0][2], 3)

    def test_one_step_from_victory_right(self):
        neighbors = find_neighbors((".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "D"), (
            ("A", "A"), ("B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(neighbors[0][0], (".", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."))
        self.assertEqual(neighbors[0][1], (("A", "A"), (
            "B", "B"), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors[0][2], 3000)

    def test_two_step_from_victory_first_child(self):
        neighbors = find_neighbors(("A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "D"), (
            ("A", "."), ("B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(neighbors[0][0], (".", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "D"))
        self.assertEqual(neighbors[0][1], (("A", "A"), (
            "B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(neighbors[0][2], 3)

    def test_two_step_from_victory_second_child(self):
        neighbors = find_neighbors(("A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "D"), (
            ("A", "."), ("B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(neighbors[1][0], ("A", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."))
        self.assertEqual(neighbors[1][1], (("A", "."), (
            "B", "B"), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors[1][2], 3000)

    def test_blocked_path_left(self):
        neighbors = find_neighbors(("D", "A", ".", ".", ".", ".", ".", ".", ".", ".", "."), (
            ("A", "."), ("B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0][0], ("D", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."))
        self.assertEqual(neighbors[0][1], (("A", "A"), (
            "B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(neighbors[0][2], 2)

    def test_blocked_path_right(self):
        neighbors = find_neighbors((".", ".", ".", ".", ".", ".", ".", ".", ".", "A", "D"), (
            ("A", "."), ("B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0][0], (".", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "D"))
        self.assertEqual(neighbors[0][1], (("A", "A"), (
            "B", "B"), ("C", "C"), ("D", ".")))
        self.assertEqual(neighbors[0][2], 8)

    def test_leaving_room(self):
        neighbors = find_neighbors((".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."), (
            ("B", "B"), ("A", "A"), ("C", "C"), ("D", "D")))
        self.assertEqual(len(neighbors), FREE_SPOT_COUNT + FREE_SPOT_COUNT)
        self.assertEqual(neighbors[0][0], ("B", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."))
        self.assertEqual(neighbors[0][1], (("B", "."), (
            "A", "A"), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors[0][2], 30)

    def test_leaving_room(self):
        neighbors = find_neighbors(("A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."), (
            ("B", "B"), ("A", "."), ("C", "C"), ("D", "D")))
        for neighbor in neighbors:
            print(neighbor[0])
        self.assertEqual(len(neighbors), 2 * (FREE_SPOT_COUNT - 1))
        self.assertEqual(neighbors[0][0], ("A", "B", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."))
        self.assertEqual(neighbors[0][1], (("B", "."), (
            "A", "."), ("C", "C"), ("D", "D")))
        self.assertEqual(neighbors[0][2], 20)


if __name__ == '__main__':
    unittest.main()
