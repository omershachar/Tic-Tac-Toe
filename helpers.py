"""
helpers.py -- file for storing all the game functions
"""

from constants import *
import os

def reset_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
                f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
                f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    reset_screen()
    print(board)

def print_user_message(turn, prev_turn):
    if prev_turn == turn: # If an invalid turn occurred, let the player know
        print("Invalid spot selected, Please pick another.")
    print("Player " + str((turn % 2) +1) + "'S turn: Pick your spot or press q to quit")

def check_turn(turn):
    if turn %2 == 0: return 'O'
    else: return 'X'

def check_game_status(spots, turn):
    horizontal_win = (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9])

    vertical_win = (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
        or (spots[3] == spots[6] == spots[9])

    diagonal_win = (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7])
    
    if horizontal_win or vertical_win or diagonal_win:
        return False, True, False # playing = False, Complete = True, tie = False
    elif turn > 8:
        return False, True, True
    else: return True, False, False

def print_game_result(complete, turn, tie):
    # reset_screen()
    draw_board(spots)
    if complete:
        if (check_turn(turn) == 'X'): print("Player 1 Wins!") # X win
        else: print("Player 2 Wins!") # O win
    elif tie: print("It's a Tie...") # Tie
    else: print("Exiting...") # pressed q