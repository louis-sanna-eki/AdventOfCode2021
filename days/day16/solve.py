import math

file = open('days/day16/input.txt', 'r')
raw_transmission = file.read()
file.close()

BASE = 16
NUM_OF_BITS = 4
VERSION_HEADER_LENGTH = 3
TYPE_HEADER_LENGTH = 3
BLOCK_LENGTH = 4


def parse_hex(char):
    return bin(int(char, BASE))[2:].zfill(NUM_OF_BITS)


def parse_first_value(transmission, _type, version):
    index = VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH
    bit_blocks = []
    while True:
        bit_blocks.append(transmission[index+1:index+1+4])
        if index > len(transmission):
            break
        if transmission[index] == "0":
            break
        index += 5
    length = index + 4 + 1  # block length + 0 indexing
    decimal = int(''.join(bit_blocks), 2)
    return {
        "_type": _type,
        "binary": transmission[0:length],
        "decimal": decimal,
        "length": length,
        "version": version
    }


def parse_first_operator(transmission, _type, version):
    index = VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH
    length_type = transmission[index]
    index += 1
    packets = []
    length = 0
    if length_type == "0":
        sub_packets_length = int(transmission[index:index+15], 2)
        index += 15
        packets = parse_binary(transmission[index:index+sub_packets_length])
        length = index + sub_packets_length
    elif length_type == "1":
        sub_packets_count = int(transmission[index:index+11], 2)
        index += 11
        packets = parse_binary(transmission[index:], sub_packets_count)
        length = index + sum(packet["length"] for packet in packets)
    else:
        raise NotImplementedError
    return {
        "_type": _type,
        "length": length,
        "length_type": length_type,
        "packets": packets,
        "version": version
    }


def parse_first_packet(transmission):
    version_header = transmission[:VERSION_HEADER_LENGTH]
    version = int(version_header, 2)
    type_header = transmission[VERSION_HEADER_LENGTH:
                               VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH]
    _type = int(type_header, 2)
    if _type == 4:
        return parse_first_value(transmission, _type, version)
    return parse_first_operator(transmission, _type, version)


def parse_binary(binary, max_packet=math.inf):
    result = []
    index = 0
    packet_count = 0
    while True:
        if index >= len(binary):
            break
        if packet_count >= max_packet:
            break
        first_packet = parse_first_packet(binary[index:])
        result.append(first_packet)
        packet_count += 1
        index += first_packet["length"]
    return result


def sum_version(packet):
    result = 0
    result += packet["version"]
    if "packets" in packet:
        result += sum(sum_version(sub_packet)
                      for sub_packet in packet["packets"])
    return result


def parse(raw_transmission):
    binaries = list(map(parse_hex, raw_transmission))
    binary = ''.join(binaries)
    # at max on packet as the outermost layer
    return parse_binary(binary, max_packet=1)


def compute_packet_version_sum(raw_transmission):
    [packet] = parse(raw_transmission)
    return sum_version(packet)


def compute_value(packet):
    if packet["_type"] == 4:
        return packet["decimal"]
    if packet["_type"] == 0:
        return sum(compute_value(packet) for packet in packet["packets"])
    if packet["_type"] == 1:
        return math.prod(compute_value(packet) for packet in packet["packets"])
    if packet["_type"] == 2:
        return min(compute_value(packet) for packet in packet["packets"])
    if packet["_type"] == 3:
        return max(compute_value(packet) for packet in packet["packets"])
    if packet["_type"] == 5:
        [first_packet, second_packet] = packet["packets"]
        greater = compute_value(first_packet) > compute_value(second_packet)
        return 1 if greater else 0
    if packet["_type"] == 6:
        [first_packet, second_packet] = packet["packets"]
        lesser = compute_value(first_packet) < compute_value(second_packet)
        return 1 if lesser else 0
    if packet["_type"] == 7:
        [first_packet, second_packet] = packet["packets"]
        equal = compute_value(first_packet) == compute_value(second_packet)
        return 1 if equal else 0
    raise NotImplementedError


[packet] = parse(raw_transmission)
result = compute_value(packet)

print(result)
