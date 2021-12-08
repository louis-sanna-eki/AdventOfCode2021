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


def get_possible_numbers(pattern, number_by_pattern):
    result = []
    candidate_numbers = numbers_by_segment_count[len(pattern)]
    for number in candidate_numbers:
        if number not in number_by_pattern.values():
            result.append(number)
    return result


def build_possible_mappings(patterns):
    number_by_pattern_mappings = [{}]
    for pattern in patterns:
        new_number_by_pattern_mappings = []
        for mapping in number_by_pattern_mappings:
            possible_numbers = get_possible_numbers(pattern, mapping)
            for number in possible_numbers:
                number_by_pattern = mapping.copy()
                number_by_pattern[pattern] = number
                new_number_by_pattern_mappings.append(number_by_pattern)
        number_by_pattern_mappings = new_number_by_pattern_mappings
    return number_by_pattern_mappings


for line in lines:
    [raw_patterns, raw_outputs] = line.split(' | ')
    patterns = raw_patterns.split(' ')
    outputs = raw_outputs.split(' ')
    # for multiple, output in enumerate(outputs):
    #     result += compute_value(output, patterns) * 10**multiple

print(build_possible_mappings(patterns))
print(len(build_possible_mappings(patterns)))
print(result)
