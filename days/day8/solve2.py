import functools

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
    1: {'c', 'f'},
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


def signature_key(signature1, signature2):
    if signature1['intersection_cardinal'] < signature2['intersection_cardinal']:
        return -1
    elif signature1['intersection_cardinal'] > signature2['intersection_cardinal']:
        return 1
    elif signature1['cardinal'] > signature2['cardinal']:
        return 1
    elif signature1['cardinal'] < signature2['cardinal']:
        return -1
    elif signature1['signed_cardinal'] > signature2['signed_cardinal']:
        return 1
    elif signature1['signed_cardinal'] < signature2['signed_cardinal']:
        return -1
    else:
        return 0


def build_intersection_signature(signed_number, pattern_by_number):
    result = []
    for number in pattern_by_number.keys():
        signed_pattern = pattern_by_number[signed_number]
        pattern = pattern_by_number[number]
        intersection_cardinal = len(
            signed_pattern.intersection(pattern))
        cardinal = len(pattern)
        signed_cardinal = len(signed_pattern)
        signature = {'intersection_cardinal': intersection_cardinal,
                     'cardinal': cardinal, 'signed_cardinal': signed_cardinal}
        result.append(signature)
    return sorted(result, key=functools.cmp_to_key(signature_key))


def signatures_key(signature1, signature2):
    for i in range(0, len(signature1)):
        key = signature_key(signature1[i], signature2[i])
        if key != 0:
            return key
    return 0


def build_signatures(pattern_by_number):
    result = []
    for number in pattern_by_number.keys():
        signature = build_intersection_signature(number, pattern_by_number)
        print(signature)
        result.append(signature)
    result.sort(key=functools.cmp_to_key(signatures_key))
    return result


def is_mapping_coherent(number_by_pattern):
    pattern_by_number = {number: set(pattern) for pattern,
                         number in number_by_pattern.items()}
    signatures = build_signatures(pattern_by_number)
    original_signatures = build_signatures(segments_by_number)
    result = True
    for i in range(0, len(signatures)):
        for j in range(0, len(signatures)):
            if signatures[i][j]['intersection_cardinal'] != original_signatures[i][j]['intersection_cardinal']:
                return False
            if signatures[i][j]['cardinal'] != original_signatures[i][j]['cardinal']:
                return False
            if signatures[i][j]['signed_cardinal'] != original_signatures[i][j]['signed_cardinal']:
                return False
    return result


def find_coherent_mapping(patterns):
    possible_mappings = build_possible_mappings(patterns)
    result = None
    for mapping in possible_mappings:
        if is_mapping_coherent(mapping):
            if result is not None:
                print(result)
                print(mapping)
                raise Exception("Several coherent mapping found")
            result = mapping
    return result


def sort_string(string_to_sort):
    return ''.join(sorted(string_to_sort))


for line in lines:
    [raw_patterns, raw_outputs] = line.split(' | ')
    patterns = raw_patterns.split(' ')
    outputs = raw_outputs.split(' ')
    for multiple, output in enumerate(outputs):
        mapping = find_coherent_mapping(map(sort_string, patterns))
        print(mapping)
        result += mapping[sort_string(output)] * 10**multiple

print(find_coherent_mapping(patterns))
print(result)
