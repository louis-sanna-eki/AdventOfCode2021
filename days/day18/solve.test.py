import unittest
from solve import (add, find_number_to_explode, magnitude,
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

    def test_magnitude(self):
        number = parse_number(
            "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
        self.assertEqual(magnitude(number), 1384)

    def test_magnitude_1(self):
        number = parse_number(
            "[[[[1,1],[2,2]],[3,3]],[4,4]]")
        self.assertEqual(magnitude(number), 445)

    def test_magnitude_2(self):
        number = parse_number(
            "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
        self.assertEqual(magnitude(number), 3488)

    def test_add(self):
        number_1 = parse_number(
            "[[[[4,3],4],4],[7,[[8,4],9]]]")
        number_2 = parse_number(
            "[1,1]")
        number = add(number_1, number_2)
        self.assertEqual(number_to_string(number),
                         "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

    def test_add_2(self):
        number_1 = parse_number(
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
        number_2 = parse_number(
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
        number = add(number_1, number_2)
        self.assertEqual(number_to_string(number),
                         "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")

    def test_add_3(self):
        number_1 = parse_number(
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
        number_2 = parse_number(
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]")
        number = add(number_1, number_2)
        self.assertEqual(number_to_string(number),
                         "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]")

    def test_add_4(self):
        number_1 = parse_number(
            "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]")
        number_2 = parse_number(
            "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]")
        number = add(number_1, number_2)
        self.assertEqual(number_to_string(number),
                         "[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]")

    def test_add_5(self):
        number_1 = parse_number(
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]")
        number_2 = parse_number(
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]")
        number = add(number_1, number_2)
        self.assertEqual(number_to_string(number),
                         "[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]")


if __name__ == '__main__':
    unittest.main()
