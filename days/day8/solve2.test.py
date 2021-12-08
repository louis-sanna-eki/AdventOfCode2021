import unittest
from solve2 import compute_value


class TestStringMethods(unittest.TestCase):

    def test_trivial_case(self):
        self.assertEqual(compute_value([], []), 0)


if __name__ == '__main__':
    unittest.main()
