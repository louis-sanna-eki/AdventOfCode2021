file = open('input.txt', 'r')
lines = file.read().splitlines()
depths = list(map(int, lines))

result = 0
currentDepth = depths[0]
for depth in depths:
    if depth > currentDepth:
        result += 1
    currentDepth = depth

print(result)

file.close()
