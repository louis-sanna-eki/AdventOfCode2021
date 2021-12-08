file = open('days/day8/input.txt', 'r')
lines = file.read().splitlines()
file.close()

result = 0

segment_count_by_number = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

segments_by_number = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'd'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

numbers_by_segment_count = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}


def get_digit(output):
    candidate_numbers = numbers_by_segment_count[len(output)]
    if len(candidate_numbers) == 1:
        return candidate_numbers[0]
    return None


def compute_value(output, patterns):
    digit = get_digit(output)
    if type(digit) is int:
        return digit
    return 0


for line in lines:
    [raw_patterns, raw_outputs] = line.split(' | ')
    patterns = raw_patterns.split(' ')
    outputs = raw_outputs.split(' ')
    for multiple, output in enumerate(outputs):
        result += compute_value(output, patterns) * 10**multiple

print(result)
