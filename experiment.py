board = [[' ', ' ', ' '],
         ['X', '0', 'X'],
         [' ', ' ', ' ']]


def displayBoard(board):
    '''Shows a 3x3 game board!!'''
    print('|---|---|---|')
    for row in board:
        for i in range(len(row)):
            if i == 0:
                print('|', row[i], end='')
            elif i == len(row)-1:
                print(row[i], '|')
            else:
                print(' |', row[i], end=' | ')
        print('|---|---|---|')


displayBoard(board)
