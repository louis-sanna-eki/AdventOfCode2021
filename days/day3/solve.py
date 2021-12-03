file = open('days/day3/input.txt', 'r')
lines = file.read().splitlines()
binaries = list(map(lambda line: list(map(int, line)), lines))
file.close()

binaryCount = len(binaries)
binaryLength = len(binaries[0])


def get_gamma(multiple):
    oneCount = 0
    for binary in binaries:
        if binary[- 1 - multiple] == 1:
            oneCount += 1
    return 1 if oneCount >= (binaryCount - oneCount) else 0


def get_epsilon(multiple):
    return 0 if get_gamma(multiple) else 1


epsilon = 0
gamma = 0

for multiple in range(0, binaryLength):
    epsilon += get_epsilon(multiple) * 2**multiple
    gamma += get_gamma(multiple) * 2**multiple

result = gamma * epsilon

print(result)
