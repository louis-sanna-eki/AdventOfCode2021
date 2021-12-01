file = open('./input.txt', 'r')
lines = file.read().splitlines()
depths = list(map(int, lines))

result = 0
currentDepthSum = depths[0] + depths[1] + depths[2]
for index in range(3, len(depths)):
    nextDepthSum = currentDepthSum + depths[index] - depths[index - 3]
    if nextDepthSum > currentDepthSum:
        result += 1
    currentDepthSum = nextDepthSum

print(result)

file.close()
