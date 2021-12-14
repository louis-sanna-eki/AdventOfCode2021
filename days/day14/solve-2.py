import math
from collections import defaultdict

file = open('days/day14/input.txt', 'r')
[raw_template, raw_insertions] = file.read().split("\n\n")
file.close()


def parse_insertion(raw_insertion):
    [pair, new] = raw_insertion.split(" -> ")
    return {"pair": pair, "insert": new}


template = raw_template
insertions = list(map(parse_insertion, raw_insertions.splitlines()))
insert_by_pair = {insertion["pair"]: insertion["insert"]
                  for insertion in insertions}

NUMBER_OF_STEPS = 40


first_template_letter = template[0]
last_template_letter = template[-1]
count_by_pair = defaultdict(lambda: 0)

for index, letter in enumerate(template[:-1]):
    next_letter = template[index + 1]
    pair = letter + next_letter
    count_by_pair[pair] += 1

for step in range(1, NUMBER_OF_STEPS + 1):
    new_count_by_pair = defaultdict(lambda: 0)
    for pair, count in count_by_pair.items():
        if pair not in insert_by_pair:
            new_count_by_pair[pair] = count
            continue
        insert = insert_by_pair[pair]
        [first_letter, second_letter] = pair
        new_left_pair = first_letter + insert
        new_right_pair = insert + second_letter
        new_count_by_pair[new_left_pair] += count
        new_count_by_pair[new_right_pair] += count
    count_by_pair = new_count_by_pair

count_by_letter = defaultdict(lambda: 0)

for pair, count in count_by_pair.items():
    [first_letter, second_letter] = pair
    count_by_letter[first_letter] += count
    count_by_letter[second_letter] += count

count_by_letter[first_template_letter] += 1  # Hack to count every letter twice
count_by_letter[last_template_letter] += 1

max = -math.inf
min = math.inf
for letter, count in count_by_letter.items():
    if count > max:
        max = count
    if count < min:
        min = count

result = int((max - min) / 2)  # each letter has been counted twice

print(result)
