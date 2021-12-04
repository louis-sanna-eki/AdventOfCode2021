file = open('days/day4/input.txt', 'r')
lines = file.read().splitlines()
file.close()

drawnNumbers = list(map(int, lines[0].split(',')))

boards = []
board = []
for index, line in enumerate(lines[1:-1]):
    boardIndex = index % 6
    if (boardIndex == 0):
        board = []
        continue
    board.append(list(map(int, line.split())))
    if (boardIndex == 5):
        boards.append(board)


print(drawnNumbers)
print(boards)
