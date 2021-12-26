import unittest
from solve import find_neighbors

HALLWAY_LENGTH = 11

x_by_letter = {"A": 2, "B": 3, "C": 4, "D": 5}


class TestAmphipod(unittest.TestCase):

    def test_trivial_case(self):
        neighbors = find_neighbors(
            ["."] * HALLWAY_LENGTH, [["A", "A"], ["B", "B"], ["C", "C"], ["D", "D"]])
        self.assertEqual(neighbors, [])

    def test_one_step_to_victory(self):
        neighbors = find_neighbors(
            ["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ], [[".", "A"], ["B", "B"], ["C", "C"], ["D", "D"]])
        self.assertEqual(neighbors, [["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ], [
                         [".", "A"], ["B", "B"], ["C", "C"], ["D", "D"]]])


if __name__ == '__main__':
    unittest.main()
