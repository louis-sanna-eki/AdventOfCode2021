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

def is_straight(vent):
    if vent['start']['x'] == vent['end']['x']:
        return True
    if vent['start']['y'] == vent['end']['y']:
        return True
    return False

for vent in vents:
    if not is_straight(vent):
        continue
    x_start = vent['start']['x'] if vent['start']['x'] < vent['end']['x'] else vent['end']['x']
    x_end = vent['end']['x'] if vent['start']['x'] < vent['end']['x'] else vent['start']['x']
    for x in range(x_start, x_end+1):
        y_start = vent['start']['y'] if vent['start']['y'] < vent['end']['y'] else vent['end']['y']
        y_end = vent['end']['y'] if vent['start']['y'] < vent['end']['y'] else vent['start']['y']
        for y in range(y_start, y_end+1):
            floor[x][y] += 1

overlappingCount = 0

for x in range(0, FLOOR_SIZE):
    for y in range(0, FLOOR_SIZE):
        if floor[x][y] > 1:
            overlappingCount += 1

print(overlappingCount)