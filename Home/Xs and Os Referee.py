'''
Tic Tac Toe Referee

You will be the referee for this games results.
You are given a result of a game and you must
determine if the game ends in a win or a draw as
well as who will be the winner. Make sure to return
"X" if the X-player wins and "O" if the O-player
wins. If the game is a draw, return "D".

A game's result is presented as a list of strings,
where "X" and "O" are players' marks and "." is
the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
'''

from typing import List

def checkio(game_result: List[str]) -> str:
    board = []
    for i in game_result:
        board.append(list(i))

    # horizontal win (use set or .count)
    for row in board:
        # print(row.count(row[0]))
        if len(set(row)) == 1:
            if row[0] == 'X':
                return 'X'
            elif row[0] == 'O':
                return 'O'
            else:
                continue

    # vertical win
    i = 0
    while i < len(board):
        col = set()
        for row in board:
            col.add(row[i])
        if len(col) == 1 and list(col)[0] != '.':
            return list(col)[0]
        i+=1

    # diagonal win
    diag_1, diag_2 = [], []
    for num in range(0,3):
        diag_1.append(board[num][num])
        diag_2.append(board[num][-(num+1)])
    print(diag_2)
    if diag_1.count(diag_1[0]) == 3 and diag_1[0] != '.':
        return diag_1[0]
    elif diag_2.count(diag_2[0]) == 3 and diag_2[0] != '.':
        return diag_2[0]

    return 'D'


print(checkio([
        "..O",
        "XOX",
<<<<<<< HEAD
        "O.."]))
=======
        "O.."]))
>>>>>>> d658cf25cc635e58a9d00e5893ca6ebfb617cca9
