import unittest
from solve import parse, compute_packet_version_sum


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

    def test_operator_0_packets(self):
        [operator] = parse("38006F45291200")
        self.assertEqual(len(operator["packets"]), 2)

    def test_operator_0_packets_subpackets(self):
        [operator] = parse("38006F45291200")
        self.assertEqual(operator["packets"][0]["decimal"], 10)
        self.assertEqual(operator["packets"][1]["decimal"], 20)

    def test_operator_1_packets(self):
        [operator] = parse("EE00D40C823060")
        self.assertEqual(len(operator["packets"]), 3)

    def test_operator_1_packets_decimal(self):
        [operator] = parse("EE00D40C823060")
        self.assertEqual(operator["packets"][0]["decimal"], 1)
        self.assertEqual(operator["packets"][1]["decimal"], 2)
        self.assertEqual(operator["packets"][2]["decimal"], 3)

    def test_packet_version_sum_0(self):
        self.assertEqual(compute_packet_version_sum("8A004A801A8002F478"), 16)

    def test_packet_version_sum_1(self):
        self.assertEqual(compute_packet_version_sum(
            "620080001611562C8802118E34"), 12)

    def test_packet_version_sum_2(self):
        self.assertEqual(compute_packet_version_sum(
            "C0015000016115A2E0802F182340"), 23)

    def test_packet_version_sum_3(self):
        self.assertEqual(compute_packet_version_sum(
            "A0016C880162017C3686B18A3D4780"), 31)


if __name__ == '__main__':
    unittest.main()
