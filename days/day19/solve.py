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

CRITERIA = 12

# list of all 3D rotation found on https://github.com/Two9A/advent-2021/blob/main/37.py
rotations = [
    lambda a: (a[0],  a[1],  a[2]),
    lambda a: (a[1],  a[2],  a[0]),
    lambda a: (a[2],  a[0],  a[1]),
    lambda a: (-a[0],  a[2],  a[1]),
    lambda a: (a[2],  a[1], -a[0]),
    lambda a: (a[1], -a[0],  a[2]),
    lambda a: (a[0],  a[2], -a[1]),
    lambda a: (a[2], -a[1],  a[0]),
    lambda a: (-a[1],  a[0],  a[2]),
    lambda a: (a[0], -a[2],  a[1]),
    lambda a: (-a[2],  a[1],  a[0]),
    lambda a: (a[1],  a[0], -a[2]),
    lambda a: (-a[0], -a[1],  a[2]),
    lambda a: (-a[1],  a[2], -a[0]),
    lambda a: (a[2], -a[0], -a[1]),
    lambda a: (-a[0],  a[1], -a[2]),
    lambda a: (a[1], -a[2], -a[0]),
    lambda a: (-a[2], -a[0],  a[1]),
    lambda a: (a[0], -a[1], -a[2]),
    lambda a: (-a[1], -a[2],  a[0]),
    lambda a: (-a[2],  a[0], -a[1]),
    lambda a: (-a[0], -a[2], -a[1]),
    lambda a: (-a[2], -a[1], -a[0]),
    lambda a: (-a[1], -a[0], -a[2]),
]


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


def find_rotation(pairs):
    for rotation in rotations:
        translations = dict()
        for pair in pairs:
            [(x, y, z), (_x, _y, _z)] = pair
            (r_x, r_y, r_z) = rotation((_x, _y, _z))
            (dx, dy, dz) = (x - r_x, y - r_y, z - r_z)
            translations[(dx, dy, dz)] = True
        if len(translations) == 1:
            return rotation
    raise Exception("Not valid rotation found")


def find_transformation(pairs):
    rotation = find_rotation(pairs)
    [(x, y, z), (_x, _y, _z)] = pairs[0]
    (r_x, r_y, r_z) = rotation((_x, _y, _z))
    (dx, dy, dz) = (x - r_x, y - r_y, z - r_z)
    return lambda point: (rotation(point)[0] + dx, rotation(point)[1] + dy, rotation(point)[2] + dz)


def comp2(f1, f2):  # from https://stackoverflow.com/questions/6900241/python-function-composition-max-recursion-depth-error-scope
    return lambda *args, **kwargs: f1(f2(*args, **kwargs))


def find_transformations_by_scanner_index(scanners):
    transformation_by_scanner_index = dict()
    transformation_by_scanner_index[0] = lambda a: a
    while True:
        if len(transformation_by_scanner_index) == len(scanners):
            return transformation_by_scanner_index
        for scanner_index, scanner in enumerate(scanners):
            for known_scanner_index, known_transformation in transformation_by_scanner_index.copy().items():
                if known_scanner_index == scanner_index:
                    continue
                known_scanner = scanners[known_scanner_index]
                matching_pairs = find_matching_pairs(known_scanner, scanner)
                if len(matching_pairs) < 3:
                    continue
                transformation = find_transformation(matching_pairs)
                transformation_by_scanner_index[scanner_index] = comp2(
                    known_transformation, transformation)


def debug():
    transformation_by_scanner_index = find_transformations_by_scanner_index(scanners)
    print(transformation_by_scanner_index)
    matching_pairs = find_matching_pairs(scanners[0], scanners[1])
    transformation = transformation_by_scanner_index[1]
    for pair in matching_pairs:
        # print(pair)
        [(x, y, z), (_x, _y, _z)] = pair
        print((x, y, z), transformation((_x, _y, _z)))


def part1():
    transformation_by_scanner_index = find_transformations_by_scanner_index(scanners)
    grid = dict()
    for scanner_index, scanner in enumerate(scanners):
        transformation = transformation_by_scanner_index[scanner_index]
        for point in scanner:
            transformed_point = transformation(point)
            grid[transformed_point] = True
    result = len(grid)
    print(result)


def part2():
    transformation_by_scanner_index = find_transformations_by_scanner_index(
        scanners)
    manhattans = list()
    for scanner_index, scanner in enumerate(scanners):
        for _scanner_index, _scanner in enumerate(scanners):
            if _scanner_index == scanner_index:
                continue
            (x, y, z) = transformation_by_scanner_index[scanner_index]((0, 0, 0))
            (_x, _y, _z) = transformation_by_scanner_index[_scanner_index]((0, 0, 0))
            manhattan = abs(x - _x) + abs(y - _y) + abs(z - _z)
            manhattans.append(manhattan)
    result = max(manhattans)
    print(result)


part2()
