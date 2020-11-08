"""
 Tac Toe Player
"""

import math
import random
import copy
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
    nx = 0
    no = 0
    for i in board:
        for j in i:
            if j == "X":
                nx += 1
            elif j == "O":
    
                no += 1
            
    if no >= nx:
        return "X"
    else:
        return "O"



    """
    Returns player who has the next turn on a board.
    """
    


def actions(board):
    acs = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                temp = []
                temp.append(i)
                temp.append(j)
                acs.append(temp)
    return acs            


def result(board, action1):
    newboard = copy.deepcopy(board)
    i = actions(board)

    action = []
    action.append(action1[0])
    action.append(action1[1])

    if action in i:
        newboard[action[0]][action[1]] = player(board)
        return newboard 
    else:
        raise  Exception("Why ü do invalid müv?")
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    rowcoldiag = []
    for i in board:
        rowcoldiag.append(i)
    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            a = board[j][i]
            temp.append(a)
        rowcoldiag.append(temp)
    rowcoldiag.append([board[0][0], board[1][1], board[2][2]])
    rowcoldiag.append([board[2][0], board[1][1], board[0][2]])
    for i in rowcoldiag:
        a = []
        for j in i:
            if not j in a:
                a.append(j)
        if len(a) == 1:
            if not a[0] == EMPTY:
                return a[0]

    return None            
                    




def terminal(board):
    if not winner(board) == None:
        return True
    
    for i in board:
        for j in i:
            if j == EMPTY:
                return False 
    return True            
def utility(board):
    if winner(board) == "X":
        return 1 
    elif winner(board) == "O":
        return -1
    else:
        return 0             

def maxvalue(board):
    if terminal(board):
        return [utility(board), ()]
    v = [-90876976, ()]
    for i in actions(board):
        a = minvalue(result(board, i))
        if a[0] > v[0]:
            v[0] = a[0]
            v[1] = i
    return v

def minvalue(board):
    if terminal(board):
        return [utility(board), ()]
    v = [90876976, ()]
    for i in actions(board):
        a = maxvalue(result(board, i))
        if a[0] < v[0]:
            v[0] = a[0]
            v[1] = i          
    return v    


def minimax(board):

    if terminal(board):
        return utility(board)
    elif len(actions(board)) > 7:
        return(random.choice(actions(board)))
    elif player(board) == "X":
        maxv = maxvalue(board)
        return maxv[1]
    elif player(board) == "O":
        minv = minvalue(board)
        return minv[1]
