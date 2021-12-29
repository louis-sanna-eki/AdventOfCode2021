file = open('days/day25/input.txt', 'r')
lines = file.read().splitlines()
file.close()

floor = [list(line) for line in lines]

max_height = len(floor)
max_width = len(floor[0])


def new_floor(_floor):
    new_floor = list()
    for y in range(0, len(_floor)):
        new_floor.append(list())
        for x in range(0, len(_floor[y])):
            new_floor[y].append(_floor[y][x])
    return new_floor


def move_east(_floor):
    count = 0
    c_floor = new_floor(_floor)
    for y in range(0, len(_floor)):
        for x in range(0, len(_floor[y])):
            if _floor[y][x] != ">":
                continue
            next_x = (x + 1) % max_width
            if _floor[y][next_x] != ".":
                continue
            c_floor[y][next_x] = ">"
            c_floor[y][x] = "."
            count += 1
    return c_floor, count


def move_south(_floor):
    count = 0
    c_floor = new_floor(_floor)
    for y in range(0, len(c_floor)):
        for x in range(0, len(c_floor[y])):
            if _floor[y][x] != "v":
                continue
            next_y = (y + 1) % max_height
            if _floor[next_y][x] != ".":
                continue
            c_floor[next_y][x] = "v"
            c_floor[y][x] = "."
            count += 1
    return c_floor, count


def step(_floor):
    east_floor, east_count = move_east(_floor)
    south_floor, south_count = move_south(east_floor)
    return south_floor, (east_count + south_count)


def part1():
    step_count = 0
    _floor = floor
    while True:
        step_count += 1
        _floor, count = step(_floor)
        if count == 0:
            break
    print(step_count)


part1()
