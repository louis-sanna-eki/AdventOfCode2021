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

OFFSET = 50
MOTOR_SIZE = 110

motor = [[[False] * MOTOR_SIZE for _ in range(MOTOR_SIZE)]
         * MOTOR_SIZE for _ in range(MOTOR_SIZE)]


def apply(motor, step):  # side-effect
    action, x_coords, y_coords, z_coords = step
    for x in range(x_coords[0]+OFFSET, x_coords[1]+1+OFFSET):
        for y in range(y_coords[0]+OFFSET, y_coords[1]+1+OFFSET):
            for z in range(z_coords[0]+OFFSET, z_coords[1]+1+OFFSET):
                if x > 100 or x < 0:
                    continue
                if y > 100 or y < 0:
                    continue
                if z > 100 or z < 0:
                    continue
                if action == "on":
                    motor[x][y][z] = True
                    continue
                if action == "off":
                    motor[x][y][z] = False
                    continue


def count(motor):
    count = 0
    for x in range(0, 2 * OFFSET + 1):
        for y in range(0, 2 * OFFSET + 1):
            for z in range(0, 2 * OFFSET + 1):
                if motor[x][y][z]:
                    count += 1
    return count


def part1():
    for step in steps:
        apply(motor, step)
    result = count(motor)
    print(result)


part1()
