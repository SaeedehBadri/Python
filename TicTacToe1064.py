# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:04:10 2021

@author: saeedeh
"""

def onetime_board(game_matrix, flg):
    if flg == 1:
        temp = "Player 1, your move:"
        flg_out = 2
    else:
        temp = "Player 2, your move:"
        flg_out = 1
    user_input = input(temp + "\nInput an integer from 1 to 9: ")
    user_input = int(user_input)
    cc = 0 
    for r in range(0,3):
        row = ''
        for c in range(0,3):
            row = row + "|"
            cc = cc + 1
            if cc == user_input:
                if flg == 1:
                    tempx = 'O'
                else:
                    tempx = 'X'
                row = row + tempx
                game_matrix[r][c] = tempx
    return game_matrix, flg_out

def new_stopping_conditions(game_matrix):
    W = [[[0,0],[0,1],[0,2]],
          [[1,0],[1,1],[1,2]],
          [[2,0],[2,1],[2,2]],
          [[0,0],[1,0],[2,0]],
          [[0,1],[1,1],[2,1]],
          [[0,2],[1,2],[2,2]],
          [[0,0],[1,1],[2,2]],
          [[0,2],[1,1],[2,0]]]
    flg = None
    for i in W:
        flg = 1
        for j in i:
            if game_matrix[j[0]][j[1]] != 'O':
                flg = None
                break
        if flg == 1:
            break
    if flg == 1:
        return True, flg  
    flg = None
    for i in W:
        flg = 2
        for j in i:
            if game_matrix[j[0]][j[1]] != 'X':
                flg = None
                break
        if flg == 2:
            break 
    if flg == 2:
        return True, flg        
    for r in game_matrix:
        for c in r:
            if c is None:
                return False, None
    return True, None

def final_game_board():
    print("Welcome to Tic Tac Toe 1064!")
    game_matrix = [[None, None, None],
                   [None, None, None],
                   [None, None, None]]
    flg = 1
    while True:
        con, winner = new_stopping_conditions(game_matrix)
        if con == True:
            break
        game_matrix, flg = onetime_board(game_matrix, flg)
        print("*********game board*********")
        for r in game_matrix:
            row = ''
            for c in r:
                row = row + "|"
                if c is not None:
                    row = row + c 
                else:
                    row = row + '_'
            row = row + "|"
            print(row)
        print("****************************")
    if winner != None:
        print("Player "+ str(winner) +" wins!")
    print ("Game over.")
final_game_board()