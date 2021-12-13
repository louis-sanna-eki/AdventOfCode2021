file = open('days/day12/input.txt', 'r')
lines = file.read().splitlines()
file.close()

neighbors_by_cave = {}

for line in lines:
    [cave1, cave2] = line.split('-')
    if cave1 not in neighbors_by_cave:
        neighbors_by_cave[cave1] = []
    neighbors_by_cave[cave1].append(cave2)
    if cave2 not in neighbors_by_cave:
        neighbors_by_cave[cave2] = []
    neighbors_by_cave[cave2].append(cave1)

valid_paths = []
paths = [{"visited": {}, "path": ["start"], "joker": True}]

while paths:
    current_path = paths.pop()
    if current_path["path"][-1] == "end":
        valid_paths.append(current_path["path"])
        continue
    for cave in neighbors_by_cave[current_path["path"][-1]]:
        if cave == "start":
            continue
        is_second_small_visit = cave.isupper(
        ) is False and cave in current_path["visited"]
        if is_second_small_visit:
            if current_path["joker"] is False:
                continue
        new_path = {
            "visited": current_path["visited"].copy(),
            "path": current_path["path"].copy(),
            "joker": False if is_second_small_visit else current_path["joker"],
        }
        new_path["visited"][cave] = True
        new_path["path"].append(cave)
        paths.append(new_path)

result = len(valid_paths)
print(result)
