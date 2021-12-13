file = open('days/day13/input.txt', 'r')
[raw_dots, raw_folds] = file.read().split("\n\n")
file.close()

print(raw_dots)
print(raw_folds)


def parse_raw_dot(raw_dot):
    [raw_x, raw_y] = raw_dot.split(",")
    return [int(raw_x), int(raw_y)]


def parse_raw_fold(raw_fold):
    [raw_dimension, raw_line] = raw_fold.split("=")
    dimension = raw_dimension[-1]
    line_index = int(raw_line)
    return {"dimension": dimension, "line_index": line_index}


dots = list(map(parse_raw_dot, raw_dots.splitlines()))
folds = list(map(parse_raw_fold, raw_folds.splitlines()))

MAX_SIZE = 2000

paper = [[0] * MAX_SIZE for _ in range(0, MAX_SIZE)]


def fold_y(fold):
    line_y = fold["line_index"]
    for x in range(0, MAX_SIZE):
        for y in range(0, MAX_SIZE):
            if paper[y][x] == 0:
                continue
            if y <= line_y:
                continue
            new_x = x
            new_y = y - 2 * (y - line_y)
            paper[y][x] = 0
            if is_in_range(new_x, new_y):
                paper[new_y][new_x] = 1


def fold_x(fold):
    line_x = fold["line_index"]
    for x in range(0, MAX_SIZE):
        for y in range(0, MAX_SIZE):
            if paper[y][x] == 0:
                continue
            if x <= line_x:
                continue
            new_x = x - 2 * (x - line_x)
            new_y = y
            paper[y][x] = 0
            if is_in_range(new_x, new_y):
                paper[new_y][new_x] = 1


def is_in_range(x, y):
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= MAX_SIZE:
        return False
    if y >= MAX_SIZE:
        return False
    return True


for dot in dots:
    [x, y] = dot
    paper[y][x] = 1


fold_x(folds[0])


def score_paper():
    result = 0
    for x in range(0, MAX_SIZE):
        for y in range(0, MAX_SIZE):
            if paper[y][x] == 1:
                result += 1
    return result


result = score_paper()

print(result)
