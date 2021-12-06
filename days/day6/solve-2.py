file = open('days/day6/input.txt', 'r')
line = file.read()
file.close()

fishes = list(map(int,line.split(',')))

REPRODUCTION_PERIOD = 6
MATURATION_PERIOD = 2

MAX_NUMBER_DAY = 256

countByRemainingDays = [0] * (REPRODUCTION_PERIOD + MATURATION_PERIOD + 1)

for fish in fishes:
    countByRemainingDays[fish] += 1

for day in range(1, MAX_NUMBER_DAY + 1):
    reproducingFishesCount = countByRemainingDays.pop(0)
    countByRemainingDays[REPRODUCTION_PERIOD] += reproducingFishesCount
    countByRemainingDays.append(reproducingFishesCount)

result = sum(countByRemainingDays)

print(result)