'''
Tic Tac Toe is a game played by two player. 
One who can manage to put 3 input in a row, col or diagonal first is considered as winner.
Other wise it is draw. 
'''

import random

print(f'Welcome to Tic Tac Toe Game!!!\n')
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
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


def get_pos(value):
    '''get position in board from given value.
        If value is 7 then position in board is (0,2)'''

    if value % 3 == 0:  # for last column (0,2), (1,2), (2,2)
        return value//3 - 1, 2
    else:
        return value // 3, value % 3 - 1


def fillUp(r, c, player1):
    '''Fill cell according to players given input'''
    if board[r][c] is ' ':
        if player1:
            board[r][c] = 'X'
        else:
            board[r][c] = '0'
        return board
    else:
        print('This position is already filled!!!')


def winingDecision(player1, board):
    '''Check condition for draw or win for every row, col and diagonal '''
    # Condition for row
    for row in board:
        if ' ' not in row:
            x, y = row.count('X'), row.count('0')
            if x == 3:
                print('Player1 Wins!!!!')
                return 'end'
            elif y == 3:
                print('Player2 Wins!!!')
                return 'end'

    # Condition for cols
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]

        if ' ' not in col:
            x, y = col.count('X'), col.count('0')
            if x == 3:
                print('Player1 Wins!!!!')
                return 'end'
            elif y == 3:
                print('Player2 Wins!!!')
                return 'end'

    # Condition for diagonal
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if ' ' not in diagonal1:
        x, y = diagonal1.count('X'), diagonal1.count('0')

        if x == 3:
            print('Player1 Wins!!!!')
            return 'end'
        elif y == 3:
            print('Player2 Wins!!!')
            return 'end'

    elif ' ' not in diagonal2:
        x, y = diagonal2.count('X'), diagonal2.count('0')
        if x == 3:
            print('Player1 Wins!!!!')
            return 'end'
        elif y == 3:
            print('Player2 Wins!!!')
            return 'end'

    # Condition for draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return None
    print("Game Draw!!!!")
    return 'end'


def firstPlayer():
    '''Decide who plays first'''
    players = [1, 2]
    choice = random.choice(players)
    if choice == 1:
        player1, player2 = True, False  # player1 plays first
    else:
        player2, player1 = True, False  # player2 plays first

    return player1, player2


displayBoard(board)
print('\n')

player1, player2 = firstPlayer()

while True:
    if player1:
        value = int(input("Player1's Turn: "))
    else:
        value = int(input("Player2's Turn: "))

    r, c = get_pos(value)

    if fillUp(r, c, player1) == None:
        print('\n')
        continue

    checkDecision = winingDecision(player1, board)
    if checkDecision is None:
        pass
    else:
        print('\n')
        displayBoard(board)
        exit()

    print('\n')
    displayBoard(board)
    print('\n')

    # Decide who's turn
    if player1:
        player1, player2 = False, True  # Next player will be player 2
    else:
        player1, player2 = True, False  # Next player will be player 2
