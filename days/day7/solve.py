import math

file = open('days/day7/input.txt', 'r')
line = file.read()
file.close()

crabs = list(map(int,line.split(',')))

def sum_linear_serie(n):
    return n * (n + 1) / 2

crab_max = max(crabs)
fuel_min = math.inf
for position in range(0, crab_max + 1):
    fuel = 0
    for crab in crabs:
        fuel += sum_linear_serie(abs(position - crab))
    if fuel < fuel_min:
        fuel_min = fuel

print(fuel_min)