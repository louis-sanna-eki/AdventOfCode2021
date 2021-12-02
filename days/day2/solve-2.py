file = open('input.txt', 'r')
lines = file.read().splitlines()
file.close()


def parse_line(line):
    words = line.split()
    return [words[0], int(words[1])]


commands = list(map(parse_line, lines))

depth = 0
position = 0
aim = 0

for command in commands:
    direction = command[0]
    magnitude = command[1]

    if (direction == 'down'):
        aim += magnitude
    if (direction == 'up'):
        aim -= magnitude
    if (direction == 'forward'):
        position += magnitude
        depth += magnitude * aim

result = depth * position

print(result)