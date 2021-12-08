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
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'd'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'}
}

numbers_by_segment_count = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

all_segments = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}


def analyse_mapping(patterns):
    candidate_segments_per_letter = {
        'a': all_segments.copy(),
        'b': all_segments.copy(),
        'c': all_segments.copy(),
        'd': all_segments.copy(),
        'e': all_segments.copy(),
        'f': all_segments.copy(),
        'g': all_segments.copy(),
        'h': all_segments.copy(),
    }
    for pattern in patterns:
        potential_numbers = numbers_by_segment_count[len(pattern)]
        for letter in pattern:
            potential_segments = map(
                lambda number: segments_by_number[number], potential_numbers)
            potential_segments = set.union(*potential_segments)
            candidate_segments_per_letter[letter] = candidate_segments_per_letter[letter].intersection(
                potential_segments)
    print(candidate_segments_per_letter)


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
    analyse_mapping(patterns)
    for multiple, output in enumerate(outputs):
        result += compute_value(output, patterns) * 10**multiple

print(result)
