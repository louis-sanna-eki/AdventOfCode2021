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


def parse_fist_value(transmission, _type, version):
    index = VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH
    bit_blocks = []
    while True:
        bit_blocks.append(transmission[index+1:index+1+4])
        if index > len(transmission):
            break
        if transmission[index] == "0":
            break
        index += 5
    semantic_length = index + 4 + 1  # block length + 0 indexing
    remainder = semantic_length % 4
    length = semantic_length + (4 - remainder) % 4
    decimal = int(''.join(bit_blocks), 2)
    return {
        "_type": _type,
        "binary": transmission[0:length],
        "decimal": decimal,
        "length": length,
        "version": version
    }


def parse_first_packet(transmission):
    version_header = transmission[:VERSION_HEADER_LENGTH]
    version = int(version_header, 2)
    type_header = transmission[VERSION_HEADER_LENGTH:
                               VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH]
    _type = int(type_header, 2)
    if _type == 4:
        return parse_fist_value(transmission, _type, version)
    raise NotImplementedError


def parse_binary(binary):
    result = []
    index = 0
    while index < len(binary):
        first_packet = parse_first_packet(binary[index:])
        result.append(first_packet)
        index += first_packet["length"]
    return result


def parse(raw_transmission):
    binaries = list(map(parse_hex, raw_transmission))
    binary = ''.join(binaries)
    return parse_binary(binary)
