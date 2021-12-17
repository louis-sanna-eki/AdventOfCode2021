file = open('days/day15/input.txt', 'r')
transmission = file.read()
file.close()

BASE = 16
NUM_OF_BITS = 4
VERSION_HEADER_LENGTH = 3
TYPE_HEADER_LENGTH = 3
BLOCK_LENGTH = 4


def parse_hex(char):
    return bin(int(char, BASE))[2:].zfill(NUM_OF_BITS)


def parse_first_packet(transmission):
    version_header = transmission[:VERSION_HEADER_LENGTH]
    version = int(version_header, 2)
    type_header = transmission[VERSION_HEADER_LENGTH:
                               VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH]
    _type = int(type_header, 2)
    index = VERSION_HEADER_LENGTH+TYPE_HEADER_LENGTH
    bit_blocks = []
    while True:
        bit_blocks.append(transmission[index+1:index+1+4])
        if index > len(transmission):
            break
        if transmission[index] == "0":
            break
        index += 5
    decimal = int(''.join(bit_blocks), 2)
    return {
        "_type": _type,
        "binary": transmission,
        "decimal": decimal,
        "version": version
    }


def parse(transmission):
    result = []
    if (transmission == ''):
        return result
    binaries = list(map(parse_hex, transmission))
    binary_transmission = ''.join(binaries)
    packet = parse_first_packet(binary_transmission)
    result.append(packet)
    return result
