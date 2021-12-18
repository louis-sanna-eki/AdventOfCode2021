file = open('days/day15/input.txt', 'r')
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
    length = index
    if length_type == "0":
        sub_packets_length = int(transmission[index:index+15], 2)
        index += 15
        packets = parse_binary(transmission[index:index+sub_packets_length])
        length += sub_packets_length
    else:
        raise NotImplementedError
    length = VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH
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


def parse_binary(binary):
    result = []
    index = 0
    _type = None
    while True:
        if index >= len(binary):
            break
        first_packet = parse_first_packet(binary[index:])
        result.append(first_packet)
        index += first_packet["length"]
        _type = first_packet["_type"]
        if _type != 4:  # operator
            break
        if len(binary) - index <= 6:
            break
    return result


def parse(raw_transmission):
    binaries = list(map(parse_hex, raw_transmission))
    binary = ''.join(binaries)
    return parse_binary(binary)
