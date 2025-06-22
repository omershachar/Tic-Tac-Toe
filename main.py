"""
main.py -- file for storing the game loop
"""

from helpers import *
from constants import *

playing = True
complete = False
tie = False
turn = 0
prev_turn = -1

try:
    while playing:
        draw_board(spots)
        print_user_message(turn, prev_turn)
        prev_turn = turn
        choice = input() # Get input from the user
        if choice == 'q':
            playing = False
            break
        # Check if the player gave a number from 1-9
        elif choice.isdigit() and int(choice) in spots:
            # check if the spot has already been taken
            if not spots[int(choice)] in {'X', 'O'}:
                # Valid input, update the board
                turn += 1
                spots[int(choice)] = check_turn(turn)
        playing, complete , tie = check_game_status(spots, turn)
    # End of playing loop
    print_game_result(complete, turn, tie)
# End of main

except ValueError as e:
    print(f"Error: {e}")

finally:
    print("End of game")