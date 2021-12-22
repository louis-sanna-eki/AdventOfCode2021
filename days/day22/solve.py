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

print(steps)
