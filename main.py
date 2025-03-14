# from curses.ascii import isdigit
from helpers import draw_board, check_turn, check_for_win
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # If an invalid turn occurred, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, Please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1) + "'S turn: Pick your spot or press q to quit")
    # Get input from the user
    choice = input()
    if choice == 'q':
        playing = False
    # Check if the player gave a number from 1-9
    elif choice.isdigit() and int(choice) in spots:
        # check if the spot has already been taken
        if not spots[int(choice)] in {'X', 'O'}:
            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Check the game termination (winner/tie)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8 : playing = False

# Print the result outside of the main loop
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
if complete:
    # X win
    if (check_turn(turn) == 'X'): print("Player 1 Wins!")
    # O win
    else: print("Player 2 Wins!")
# Tie
else: print("It's a Tie...")

# End of main