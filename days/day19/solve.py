file = open('days/day19/input.txt', 'r')
lines = file.read().splitlines()
file.close()

scanners = list()


scanner = list()
for line in lines:
    if line.startswith('--- scanner'):
        scanner = list()
        continue
    if line == "":
        scanners.append(scanner)
        continue
    scanner.append([int(coordinate) for coordinate in line.split(",")])
scanners.append(scanner)

CRITERIA = 3


def build_fingerprint_by_point(scanner: list):
    result = dict()
    for [x, y, z] in scanner:
        fingerprint = dict()
        for [_x, _y, _z] in scanner:
            dx = abs(x - _x)
            dy = abs(y - _y)
            dz = abs(z - _z)
            fingerprint[tuple(sorted([dx, dy, dz]))] = True
        result[(x, y, z)] = fingerprint
    return result


def count_commun_deltas(fingerprint1: dict, fingerprint2: dict):
    result = 0
    for (x, y, z) in fingerprint1:
        if (x, y, z) in fingerprint2:
            result += 1
    return result


def find_matching_pairs(scanner1, scanner2):
    result = list()
    fingerprint_by_point_1 = build_fingerprint_by_point(scanner1)
    fingerprint_by_point_2 = build_fingerprint_by_point(scanner2)
    for point, fingerprint in fingerprint_by_point_1.items():
        for _point, _fingerprint in fingerprint_by_point_2.items():
            commun_count = count_commun_deltas(fingerprint, _fingerprint)
            if commun_count >= CRITERIA:
                result.append([point, _point])
    return result


def debug():
    matching_pairs = find_matching_pairs(scanners[0], scanners[1])
    for pair in matching_pairs:
        print(pair)


debug()
