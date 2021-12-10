file = open('days/day10/input.txt', 'r')
lines = file.read().splitlines()
file.close()

closing_by_opening = {'{': '}', '[': ']', '<': '>', '(': ')'}
opening_by_closing = {opening: closing for closing,
                      opening in closing_by_opening.items()}
opening = ['{', '(', '[', '<']

points_by_char = {')': 3, ']': 57, '}': 1197, '>': 25137}

result = 0


def score(line):
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
            continue
        matching = stack.pop()
        if matching != opening_by_closing[char]:
            return points_by_char[char]
    return 0


for line in lines:
    result += score(line)

print(result)
