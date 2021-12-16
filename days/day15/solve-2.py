from queue import PriorityQueue
import math


file = open('days/day15/input.txt', 'r')
lines = file.read().splitlines()
file.close()

floor = [list(map(int, line)) for line in lines]

floor_INCREASE_FACTOR = 5

original_size = len(floor)

for _ in range(0, original_size * (floor_INCREASE_FACTOR - 1)):
    floor.append([])

for x in range(0, len(floor)):
    for y in range(0, len(floor)):  # assume square input
        if x < original_size and y < original_size:
            continue
        tile_x = x // original_size
        tile_y = y // original_size
        original_x = x % original_size
        original_y = y % original_size
        new_risk = (floor[original_x][original_y] + tile_x + tile_y) % 9
        if new_risk == 0:
            new_risk = 9
        floor[x].append(new_risk)


def build_square(risk):
    return dict({"lowest_risk": math.inf,
                 "risk": risk,
                 "visited": False,
                 })


squares = [list(map(build_square, row)) for row in floor]

boundary = PriorityQueue()


def is_in_cave(x, y):
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= len(squares):
        return False
    if y >= len(squares[x]):
        return False
    return True


def update_lowest_risk(x, y, current_path_risk):
    if is_in_cave(x, y) is False:
        return
    square = squares[x][y]
    current_lowest_risk = square["lowest_risk"]
    new_risk = square["risk"] + current_path_risk
    if new_risk < current_lowest_risk:
        square["lowest_risk"] = new_risk
        boundary.put((square["lowest_risk"], [x, y]))


def visit(x, y):
    if is_in_cave(x, y) is False:
        return
    if squares[x][y]["visited"] is True:
        return
    current_path_risk = squares[x][y]["lowest_risk"]
    update_lowest_risk(x+1, y, current_path_risk)
    update_lowest_risk(x, y+1, current_path_risk)
    update_lowest_risk(x-1, y, current_path_risk)
    update_lowest_risk(x, y-1, current_path_risk)
    squares[x][y]["visited"] = True


squares[0][0]["lowest_risk"] = 0  # Set starting point
visit(0, 0)

while not boundary.empty():
    [priority, coordinates] = boundary.get()
    [x, y] = coordinates
    visit(x, y)

print(squares[-1][-1])
