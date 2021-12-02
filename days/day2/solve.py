file = open('input.txt', 'r')
lines = file.read().splitlines()
file.close()


def parse_line(line):
    words = line.split()
    return [words[0], int(words[1])]


commands = list(map(parse_line, lines))

print(commands)
