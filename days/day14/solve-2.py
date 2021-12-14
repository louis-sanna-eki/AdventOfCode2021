import math

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
count_by_pair = {}

for index, letter in enumerate(template[0:-1]):
    next_letter = template[index + 1]
    pair = letter + next_letter
    if pair not in count_by_pair:
        count_by_pair[pair] = 0
    count_by_pair[pair] += 1

for step in range(1, NUMBER_OF_STEPS + 1):
    new_count_by_pair = {}
    for pair, count in count_by_pair.items():
        if pair not in insert_by_pair:
            new_count_by_pair[pair] = count
            continue
        insert = insert_by_pair[pair]
        new_left_pair = pair[0] + insert
        new_right_pair = insert + pair[1]
        if new_left_pair not in new_count_by_pair:
            new_count_by_pair[new_left_pair] = 0
        new_count_by_pair[new_left_pair] += count
        if new_right_pair not in new_count_by_pair:
            new_count_by_pair[new_right_pair] = 0
        new_count_by_pair[new_right_pair] += count
    count_by_pair = new_count_by_pair

count_by_letter = {}

for pair, count in count_by_pair.items():
    first_letter = pair[0]
    if first_letter not in count_by_letter:
        count_by_letter[first_letter] = 0
    count_by_letter[first_letter] += count
    second_letter = pair[1]
    if second_letter not in count_by_letter:
        count_by_letter[second_letter] = 0
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
