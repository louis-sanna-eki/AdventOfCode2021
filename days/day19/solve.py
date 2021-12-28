file = open('days/day19/input.txt', 'r')
lines = file.read().splitlines()
file.close()

scanners = list()
scanner = list()

for line in lines:
    if line.startswith('--- scanner'):
        scanner = list()
        continue
    if line == "":
        scanners.append(scanner)
        continue
    scanner.append([int(coordinate) for coordinate in line.split(",")])
