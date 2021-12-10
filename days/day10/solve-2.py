file = open('days/day10/input.txt', 'r')
lines = file.read().splitlines()
file.close()

closing_by_opening = {'{': '}', '[': ']', '<': '>', '(': ')'}
opening_by_closing = {opening: closing for closing,
                      opening in closing_by_opening.items()}
opening = ['{', '(', '[', '<']

points_by_char = {')': 1, ']': 2, '}': 3, '>': 4}

result = 0


def compute_completing_stack(line):
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
            continue
        matching = stack.pop()
        if matching != opening_by_closing[char]:
            return None
    completion = []
    for opening_char in stack:
        completion.insert(0, closing_by_opening[opening_char])
    return completion


def score_completion(completion):
    result = 0
    for char in completion:
        result = result * 5 + points_by_char[char]
    return result


scores = []

for line in lines:
    completion = compute_completing_stack(line)
    print('stack', completion)
    if completion is not None:
        scores.append(score_completion(completion))

scores.sort()
result = scores[int(len(scores) / 2)]

print(result)
