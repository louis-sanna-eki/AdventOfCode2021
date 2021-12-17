file = open('days/day15/input.txt', 'r')
transmission = file.read()
file.close()

BASE = 16
NUM_OF_BITS = 4


def parse_hex(char):
    return bin(int(char, BASE))[2:].zfill(NUM_OF_BITS)


def parse(transmission):
    result = []
    if (transmission == ''):
        return result
    binaries = list(map(parse_hex, transmission))
    binary_transmission = ''.join(binaries)
    result.append({"binary": binary_transmission})
    return result
