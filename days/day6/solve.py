file = open('days/day6/input.txt', 'r')
line = file.read()
file.close()

fishes = list(map(int,line.split(',')))

REPRODUCTION_PERIOD = 6
MATURATION_PERIOD = 2

MAX_NUMBER_DAY = 80

for day in range(1, MAX_NUMBER_DAY + 1):
    for index in range(0, len(fishes)):
        if fishes[index] == 0:
            fishes[index] = REPRODUCTION_PERIOD
            fishes.append(MATURATION_PERIOD + REPRODUCTION_PERIOD)
            continue
        fishes[index] -= 1

result = len(fishes)

print(result)