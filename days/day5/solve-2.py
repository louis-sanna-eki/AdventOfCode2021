file = open('days/day5/input.txt', 'r')
lines = file.read().splitlines()
file.close()

FLOOR_SIZE = 1000
vents = []

for line in lines:
    [string_start, string_end] = line.split(' -> ')
    [start_x, start_y] = list(map(int,string_start.split(',')))
    [end_x, end_y] = list(map(int,string_end.split(',')))

    vent = { 
        'start': { 'x': start_x, 'y': start_y },
        'end': { 'x': end_x, 'y': end_y }
    }
    vents.append(vent)
    
floor = [[0] * FLOOR_SIZE for _ in range(FLOOR_SIZE)]

for vent in vents:
    x_start = vent['start']['x']
    x_end = vent['end']['x']
    y_start = vent['start']['y']
    y_end = vent['end']['y']
    x = x_start
    y = y_start
    x_step = 1 if x_start < x_end else -1
    y_step = 1 if y_start < y_end else -1
    floor[x][y] += 1
    while x != x_end or y != y_end:
        if x != x_end:
            x += x_step
        if y != y_end:
            y += y_step
        floor[x][y] += 1

overlappingCount = 0

for x in range(0, FLOOR_SIZE):
    for y in range(0, FLOOR_SIZE):
        if floor[x][y] > 1:
            overlappingCount += 1

print(overlappingCount)