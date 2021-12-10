import itertools

file = open('days/day8/input.txt', 'r')
lines = file.read().splitlines()
file.close()

result = 0

segments_by_number = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
number_by_segments = {segment: number for number,
                      segment in segments_by_number.items()}

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def sort_string(string_to_sort):
    return ''.join(sorted(string_to_sort))


def sort_patterns(patterns):
    sorted_patterns = map(lambda pattern: sort_string(pattern), patterns)
    sorted_patterns.sort()
    return sorted_patterns


def get_permutation(patterns):
    permutations = itertools.permutations(all_letters)
    for permutation in permutations:
        print('permutation', permutation)


for line in lines:
    [raw_patterns, raw_outputs] = line.split(' | ')
    patterns = raw_patterns.split(' ')
    outputs = raw_outputs.split(' ')
    for output in outputs:
        number = get_permutation(patterns)
