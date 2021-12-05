file = open('days/day5/input.txt', 'r')
lines = file.read().splitlines()
file.close()

vents = []

for line in lines:
    [start, end] = line.split(' -> ')
    vent = { 
        start: { 'x': int(start[0]), 'y': int(start[2]) },
        end: { 'x': int(end[0]), 'y': int(end[2]) }
    }
    vents.append(vent)

print(vents)