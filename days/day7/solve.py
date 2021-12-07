import math

file = open('days/day7/input.txt', 'r')
line = file.read()
file.close()

crabs = list(map(int,line.split(',')))

crab_max = max(crabs)

min_fuel = math.inf

for position in range(0, crab_max + 1):
    fuel = 0
    for crab in crabs:
        fuel += abs(position - crab)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)