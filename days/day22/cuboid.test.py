import unittest
from cuboid import Cuboid


class TestCuboid(unittest.TestCase):

    def test_trivial_intersect(self):
        cuboid = Cuboid(((0, 0), (0, 0), (0, 0)))
        result = cuboid.intersects(cuboid)
        self.assertEqual(result, True)

    def test_disjoint_intersect(self):
        cuboid = Cuboid(((0, 0), (0, 0), (0, 0)))
        result = cuboid.intersects(Cuboid(((1, 1), (0, 0), (0, 0))))
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
