import unittest
from solve import parse


class TestStringMethods(unittest.TestCase):

    def test_trivial_case(self):
        self.assertEqual(parse(""), [])

    def test_hex_to_binary(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["binary"], '110100101111111000101')

    def test_version(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["version"], 6)

    def test_type(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["_type"], 4)

    def test_decimal(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["decimal"], 2021)

    def test_length(self):
        self.assertEqual(parse("D2FE28")[0]
                         ["length"], 21)

    def test_operator_packets(self):
        [operator] = parse("38006F45291200")
        self.assertEqual(len(operator["packets"]), 2)

    def test_operator_packets_subpackets(self):
        [operator] = parse("38006F45291200")
        self.assertEqual(operator["packets"][0]["decimal"], 10)
        self.assertEqual(operator["packets"][1]["decimal"], 20)


if __name__ == '__main__':
    unittest.main()
