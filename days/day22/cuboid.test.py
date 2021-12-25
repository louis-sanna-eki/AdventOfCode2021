import unittest
from cuboid import Cuboid


class TestCuboid(unittest.TestCase):

    def test_trivial_intersect(self):
        cuboid = Cuboid([[0, 0], [0, 0], [0, 0]])
        result = cuboid.intersects(cuboid)
        self.assertEqual(result, True)

    def test_disjoint_intersect(self):
        cuboid = Cuboid([[0, 0], [0, 0], [0, 0]])
        result = cuboid.intersects(Cuboid([[1, 1], [0, 0], [0, 0]]))
        self.assertEqual(result, False)

    def test_overlapping_intersect(self):
        cuboid = Cuboid([[0, 2], [0, 0], [0, 0]])
        result = cuboid.intersects(Cuboid([[1, 1], [0, 0], [0, 0]]))
        self.assertEqual(result, True)

    def test_trivial_remove(self):
        cuboid = Cuboid([[0, 0], [0, 0], [0, 0]])
        result = cuboid.remove(Cuboid([[0, 0], [0, 0], [0, 0]]))
        self.assertEqual(len(result), 0)

    def test_remove_top(self):
        cuboid = Cuboid([[0, 1], [0, 0], [0, 0]])
        result = cuboid.remove(Cuboid([[1, 1], [0, 0], [0, 0]]))
        self.assertEqual(result[0].coordinates, [[0, 0], [0, 0], [0, 0]])

    def test_remove_bottom(self):
        cuboid = Cuboid([[0, 1], [0, 0], [0, 0]])
        result = cuboid.remove(Cuboid([[0, 0], [0, 0], [0, 0]]))
        self.assertEqual(result[0].coordinates, [[1, 1], [0, 0], [0, 0]])

    def test_remove_y_top(self):
        cuboid = Cuboid([[0, 0], [0, 1], [0, 0]])
        result = cuboid.remove(Cuboid([[0, 0], [1, 1], [0, 0]]))
        self.assertEqual(result[0].coordinates, [[0, 0], [0, 0], [0, 0]])

    def test_remove_y_bottom(self):
        cuboid = Cuboid([[0, 0], [0, 1], [0, 0]])
        result = cuboid.remove(Cuboid([[0, 0], [0, 0], [0, 0]]))
        self.assertEqual(result[0].coordinates, [[0, 0], [1, 1], [0, 0]])


if __name__ == '__main__':
    unittest.main()
