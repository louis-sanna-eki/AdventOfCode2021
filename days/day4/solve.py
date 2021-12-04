file = open('days/day4/input.txt', 'r')
lines = file.read().splitlines()
file.close()

numbers = list(map(int, lines[0].split(',')))

boards = []
board = []
for index, line in enumerate(lines[1:]):
    boardIndex = index % 6
    if (boardIndex == 0):
        board = []
        continue
    board.append(list(map(int, line.split())))
    if (boardIndex == 5):
        boards.append(board)


def is_board_won(board, drawnNumbers):
    drawnNumbersDict = {
        number: True for index, number in enumerate(drawnNumbers)
    }
    for row in board:
        markedRow = True
        for value in row:
            if value not in drawnNumbersDict:
                markedRow = False
        if markedRow:
            return True
    for columnIndex in range(0, 5):
        markedColumn = True
        for rowIndex in range(0, 5):
            value = board[rowIndex][columnIndex]
            if value not in drawnNumbersDict:
                markedColumn = False
        if markedColumn:
            return True
    return False


def score_board(board, drawnNumbers):
    drawnNumbersDict = {
        number: True for index, number in enumerate(drawnNumbers)
    }
    result = 0
    for row in board:
        for value in row:
            if value not in drawnNumbersDict:
                result += value
    return result


result = 0
for index, number in enumerate(numbers):
    drawnNumbers = numbers[0:index+1]
    for board in boards:
        if is_board_won(board, drawnNumbers):
            boardScore = score_board(board, drawnNumbers)
            print('boardScore', boardScore)
            print('number', number)
            result = boardScore * number
            break
    if result:
        break

print(result)
