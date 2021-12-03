file = open('days/day3/input.txt', 'r')
lines = file.read().splitlines()
binaries = list(map(lambda line: list(map(int, line)), lines))
file.close()

binaryCount = len(binaries)
binaryLength = len(binaries[0])


def get_bit_criteria(position, currentBinaries):
    oneCount = 0
    for binary in currentBinaries:
        if binary[position] == 1:
            oneCount += 1
    return 1 if oneCount >= (len(currentBinaries) - oneCount) else 0


oxygenBinaries = binaries.copy()
oxygenBinary = []
scrubberBinaries = binaries.copy()
scrubberBinary = []

for position in range(0, binaryLength):
    oxygenCriteria = get_bit_criteria(position, oxygenBinaries)
    oxygenBinaries = list(
        filter(
            lambda binary: binary[position] == oxygenCriteria,
            oxygenBinaries
        )
    )
    scrubberCriteria = 0 if get_bit_criteria(position, scrubberBinaries) else 1
    scrubberBinaries = list(
        filter(
            lambda binary: binary[position] == scrubberCriteria,
            scrubberBinaries
        )
    )
    if (len(oxygenBinaries) == 1):
        [oxygenBinary] = oxygenBinaries
    if (len(scrubberBinaries) == 1):
        [scrubberBinary] = scrubberBinaries


def convert_to_base_10(binary):
    result = 0
    for multiple in range(0, len(binary)):
        result += binary[-1 - multiple] * 2**multiple
    return result


oxygen = convert_to_base_10(oxygenBinary)
scrubber = convert_to_base_10(scrubberBinary)

result = oxygen * scrubber

print(oxygen * scrubber)
