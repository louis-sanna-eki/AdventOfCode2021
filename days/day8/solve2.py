import itertools

file = open('days/day8/input.txt', 'r')
lines = file.read().splitlines()
file.close()

result = 0

pattern_by_number = {
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
number_by_pattern = {segment: number for number,
                     segment in pattern_by_number.items()}

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
original_index_by_letter = {
    letter: index for index, letter in enumerate(all_letters)}


def sort_string(string_to_sort):
    return ''.join(sorted(string_to_sort))


def sort_patterns(patterns):
    sorted_patterns = list(map(lambda pattern: sort_string(pattern), patterns))
    sorted_patterns.sort()
    return sorted_patterns


original_patterns = sort_patterns(
    [pattern for number, pattern in pattern_by_number.items()])


def un_permute_pattern(pattern, permutation):
    result = ''
    index_by_letter = {
        letter: index for index, letter in enumerate(permutation)}
    for letter in pattern:
        result += all_letters[index_by_letter[letter]]
    return result


def un_permute_patterns(patterns, permutation):
    return map(
        lambda pattern: un_permute_pattern(pattern, permutation), patterns)


def get_permutation(patterns):
    permutations = itertools.permutations(all_letters)
    for permutation in permutations:
        permuted_patterns = sort_patterns(
            un_permute_patterns(patterns, permutation))
        is_valid_permutation = True
        for index in range(0, len(original_patterns)):
            if permuted_patterns[index] != original_patterns[index]:
                is_valid_permutation = False
        if is_valid_permutation:
            return permutation


result = 0

for line in lines:
    [raw_patterns, raw_outputs] = line.split(' | ')
    patterns = raw_patterns.split(' ')
    outputs = raw_outputs.split(' ')
    permutation = get_permutation(patterns)
    index_by_letter = {
        letter: index for index, letter in enumerate(permutation)}
    for index, output in enumerate(outputs):
        unpermuted_output = sort_string(
            un_permute_pattern(output, permutation))
        number_to_decode = number_by_pattern[unpermuted_output]
        result += number_to_decode * 10**(3-index)

print(result)
