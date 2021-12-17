file = open('days/day15/input.txt', 'r')
transmission = file.read()
file.close()

BASE = 16
NUM_OF_BITS = 4


def parse_hex(char):
    return bin(int(char, BASE))[2:].zfill(NUM_OF_BITS)


def parse_first_packet(transmission):
    version_header = transmission[:3]
    version = int(version_header, 2)
    type_header = transmission[3:6]
    type = int(type_header, 2)
    return {"binary": transmission, "type": type, "version": version}


def parse(transmission):
    result = []
    if (transmission == ''):
        return result
    binaries = list(map(parse_hex, transmission))
    binary_transmission = ''.join(binaries)
    packet = parse_first_packet(binary_transmission)
    result.append(packet)
    return result
