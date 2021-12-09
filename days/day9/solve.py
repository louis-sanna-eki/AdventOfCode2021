file = open('days/day9/input.txt', 'r')
lines = file.read().splitlines()
file.close()

points = list(map(lambda line: list(map(int, line)), lines))


def is_local_minimum(i, j):
    if i+1 < 100 and points[i][j] >= points[i+1][j]:
        return False
    if i-1 >= 0 and points[i][j] >= points[i-1][j]:
        return False
    if j+1 < 100 and points[i][j] >= points[i][j+1]:
        return False
    if j-1 >= 0 and points[i][j] >= points[i][j-1]:
        return False
    return True


def compute_risk(i, j):
    return 1 + points[i][j]


result = 0

for i in range(0, len(points)):
    for j in range(0, len(points[i])):
        if is_local_minimum(i, j):
            result += compute_risk(i, j)

print(result)
