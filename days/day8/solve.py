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

numbers_by_segment_count = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}


def get_number(output):
    candidate_numbers = numbers_by_segment_count[len(output)]
    if len(candidate_numbers) == 1:
        return candidate_numbers[0]
    return None


for line in lines:
    [raw_patterns, raw_outputs] = line.split(' | ')
    patterns = raw_patterns.split(' ')
    outputs = raw_outputs.split(' ')
    for output in outputs:
        number = get_number(output)
        if number in [1, 4, 7, 8]:
            result += 1

print(result)
