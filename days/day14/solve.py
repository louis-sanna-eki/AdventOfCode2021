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

NUMBER_OF_STEPS = 10


polymer = template

for step in range(1, NUMBER_OF_STEPS + 1):
    new_polymer = [polymer[0]]
    for index, letter in enumerate(polymer):
        if index == 0:
            continue
        previous_letter = polymer[index - 1]
        pair = previous_letter + letter
        print(pair)
        if pair in insert_by_pair:
            new_polymer.append(insert_by_pair[pair])
        new_polymer.append(letter)
    polymer = new_polymer

print(polymer)
