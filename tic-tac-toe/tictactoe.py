"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num=0
    o_num=0
    for row in board:
        for item in row:
            if item == X:
                x_num+=1
            elif item == O:
                o_num+=1

    if x_num > o_num:
        return O
    elif x_num == o_num:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play = player(board)
    output_board = deepcopy(board)

    i, j = action

    if output_board[i][j] == EMPTY:
        output_board[i][j] = play
    else:
        raise Exception("Invalid action")

    return output_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # vertical
    for i in range(3):
        col_arr = []
        for j in range(3):
            col_arr.append(board[j][i])

        if col_arr == [X, X, X]:
            return X
        elif col_arr == [O, O, O]:
            return O
    
    # horizontal
    for row in range(3):
        row_arr = []
        for col in range(3):
            row_arr.append(board[row][col])
        if row_arr == [X, X, X]:
            return X
        elif row_arr == [O, O, O]:
            return O
    
    # diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O

    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O

    return None            
            

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    for row in board:
        for item in row:
            if item == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    winning_player = winner(board)

    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0

def max_value(board):
    best_move = ()
    if terminal(board):
        return utility(board), best_move
    v = -100
    for action in actions(board):
        temp_val = min_value(result(board, action))[0]
        if temp_val > v:
            v = temp_val
            best_move = action
    return v, best_move


def min_value(board):
    best_move = ()
    if terminal(board):
        return utility(board), best_move
    v = 100
    for action in actions(board):
        temp_val = max_value(result(board, action))[0]
        if temp_val < v:
            v = temp_val
            best_move = action
    return v, best_move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
  
    if terminal(board):
        return None

    the_player = player(board)
    
    if the_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
