import unittest
from solve import parse_number, number_to_string


class TestDay18Methods(unittest.TestCase):

    def test_input_parsing(self):
        self.assertEqual(parse_number("[[[[[9,8],1],2],3],4]")["right"], 4)

    def test_number_to_string(self):
        self.assertEqual(number_to_string(parse_number(
            "[[[[[9,8],1],2],3],4]")), "[[[[[9,8],1],2],3],4]")


if __name__ == '__main__':
    unittest.main()
