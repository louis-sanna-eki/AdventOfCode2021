import unittest
from solve import parse


class TestStringMethods(unittest.TestCase):

    def test_trivial_case(self):
        self.assertEqual(parse(""), [])

    def test_hex_to_binary(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["binary"], '110100101111111000101000')

    def test_version(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["version"], 6)

    def test_type(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["type"], 4)


if __name__ == '__main__':
    unittest.main()
