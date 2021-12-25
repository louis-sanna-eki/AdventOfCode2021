from cuboid import Cuboid

file = open('days/day22/input.txt', 'r')
lines = file.read().splitlines()
file.close()


def parse_coords(raw_coordinates: str):  # x=-30..21
    [raw_min, raw_max] = raw_coordinates.split("=")[1].split("..")
    return [int(raw_min), int(raw_max)]


def parse(line: str):
    action, raw_coordinates = line.split(' ')
    [x_coords, y_coords, z_coords] = raw_coordinates.split(',')
    return action, parse_coords(x_coords), parse_coords(y_coords), parse_coords(z_coords)


steps = list(map(parse, lines))


def apply(cuboids, step):  # side-effect

    def add(cuboid_to_add: Cuboid):  # side-effect
        for cuboid in cuboids:
            if cuboid.intersects(cuboid_to_add):
                cuboids_to_add = cuboid_to_add.remove(cuboid)
                for sub_cuboid in cuboids_to_add:
                    add(sub_cuboid)
                return
        cuboids.append(cuboid_to_add)

    def remove(cuboid_to_remove: Cuboid):  # side effect
        new_cuboids = []
        for cuboid in cuboids:
            if cuboid.intersects(cuboid_to_remove) is False:
                new_cuboids.append(cuboid)
                continue
            new_cuboids.extend(cuboid.remove(cuboid_to_remove))
        return new_cuboids

    action, x_coords, y_coords, z_coords = step
    if action == "on":
        cuboid_to_add = Cuboid([x_coords, y_coords, z_coords])
        add(cuboid_to_add)
    if action == "off":
        cuboid_to_remove = Cuboid([x_coords, y_coords, z_coords])
        cuboids = remove(cuboid_to_remove)
    return cuboids


def count(cuboids):
    count = 0
    for cuboid in cuboids:
        count += cuboid.volume()
    return count


def part2():
    cuboids: list[Cuboid] = list()

    for step in steps:
        cuboids = apply(cuboids, step)
    result = count(cuboids)
    print(len(cuboids))
    print(result)


part2()
