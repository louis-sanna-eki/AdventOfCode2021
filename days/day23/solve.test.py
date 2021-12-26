
import unittest
from solve import find_neighbors

HALLWAY_LENGTH = 11

x_by_letter = {"A": 2, "B": 3, "C": 4, "D": 5}


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


if __name__ == '__main__':
    unittest.main()
