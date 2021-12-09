file = open('days/day9/input.txt', 'r')
lines = file.read().splitlines()
file.close()

points = list(map(lambda line: list(map(int, line)), lines))

visited = [[False] * len(lines[0]) for _ in range(len(lines))]
bassin_sizes = []


def visit_bassin(i, j):
    if i >= 100 or i < 0:
        return 0
    if j >= 100 or j < 0:
        return 0
    if visited[i][j]:
        return 0
    visited[i][j] = True
    if points[i][j] == 9:
        return 0
    return 1 + visit_bassin(i+1, j) + visit_bassin(i-1, j) + visit_bassin(i, j+1) + visit_bassin(i, j-1)


for i in range(0, len(points)):
    for j in range(0, len(points[i])):
        if visited[i][j] is False:
            bassin_size = visit_bassin(i, j)
            if bassin_size != 0:
                bassin_sizes.append(bassin_size)

bassin_sizes.sort()

print(bassin_sizes[-1] * bassin_sizes[-2] * bassin_sizes[-3])
