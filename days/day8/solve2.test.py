import unittest
from solve2 import compute_value


class TestStringMethods(unittest.TestCase):

    def test_trivial_case(self):
        self.assertEqual(compute_value([], []), 0)

    def test_singleton_segment_count(self):
        patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad',
                    'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
        self.assertEqual(compute_value(['ab'], patterns), 1)

    def test_output_with_several_digits(self):
        patterns = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad',
                    'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
        self.assertEqual(compute_value(['ab', 'ab'], patterns), 11)


if __name__ == '__main__':
    unittest.main()
