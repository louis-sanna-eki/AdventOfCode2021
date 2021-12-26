
import unittest
from diagram import Diagram

HALLWAY_LENGTH = 11

x_by_letter = {"A": 2, "B": 3, "C": 4, "D": 5}


class TestDiagram(unittest.TestCase):

    def test_trivial_case(self):
        diagram = Diagram(
            ["."] * HALLWAY_LENGTH, [["A", "A"], ["B", "B"], ["C", "C"], ["D", "D"]], 0)
        neighbors = diagram.find_neighbors()
        self.assertEqual(neighbors, [])

    def test_one_step_from_victory(self):
        diagram = Diagram(["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [
                          ["A", "."], ["B", "B"], ["C", "C"], ["D", "D"]], 0)
        neighbors = diagram.find_neighbors()
        self.assertEqual(neighbors[0].hallway, [".", ".", ".",
                         ".", ".", ".", ".", ".", ".", ".", "."])
        self.assertEqual(neighbors[0].rooms, [["A", "A"], [
            "B", "B"], ["C", "C"], ["D", "D"]])
        self.assertEqual(neighbors[0].energy, 3)


if __name__ == '__main__':
    unittest.main()
