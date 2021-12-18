import unittest
from solve import (find_number_to_explode,
                   number_to_string, parse_number, reduce)


class TestDay18Methods(unittest.TestCase):

    def test_input_parsing(self):
        self.assertEqual(parse_number("[[[[[9,8],1],2],3],4]")[
                         "right"]["value"], 4)

    def test_number_to_string(self):
        self.assertEqual(number_to_string(parse_number(
            "[[[[[9,8],1],2],3],4]")), "[[[[[9,8],1],2],3],4]")

    def test_find_number_to_explode(self):
        number = parse_number(
            "[[[[[9,8],1],2],3],4]")
        number_to_explode = find_number_to_explode(number)
        self.assertEqual(number_to_explode["left"]["value"], 9)
        self.assertEqual(number_to_explode["right"]["value"], 8)

    def test_explode_no_regular_left(self):
        number_to_reduce = parse_number(
            "[[[[[9,8],1],2],3],4]")
        number = reduce(number_to_reduce)
        self.assertEqual(number_to_string(number), "[[[[0,9],2],3],4]")

    def test_explode_no_regular_right(self):
        number_to_reduce = parse_number(
            "[7,[6,[5,[4,[3,2]]]]]")
        number = reduce(number_to_reduce)
        self.assertEqual(number_to_string(number), "[7,[6,[5,[7,0]]]]")

    def test_explode_basic(self):
        number_to_reduce = parse_number(
            "[[6,[5,[4,[3,2]]]],1]")
        number = reduce(number_to_reduce)
        self.assertEqual(number_to_string(number), "[[6,[5,[7,0]]],3]")

    def test_sequential_explode(self):
        number_to_reduce = parse_number(
            "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        number = reduce(number_to_reduce)
        self.assertEqual(number_to_string(number),
                         "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

    def test_explode_and_split(self):
        number_to_reduce = parse_number(
            "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
        number = reduce(number_to_reduce)
        self.assertEqual(number_to_string(number),
                         "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")


if __name__ == '__main__':
    unittest.main()
