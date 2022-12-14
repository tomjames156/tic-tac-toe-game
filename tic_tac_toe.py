import sys
# the_board = [
#     {"top-L": 'X', "top-M": ' ', "top-R": ' '},
#     {"mid-L": ' ', "mid-M": 'X', "mid-R": ' '},
#     {"low-L": 'X', "low-M": ' ', "low-R": 'X'}
# ] # this one is for printing it without the guides

# game_values = list(the_board.values())
# print(game_values)

# for dictionary in the_board:
#     for item in dictionary.values():
#         print(item, end=' ')
#     print() # this function prints the tictactoe board but for a different data type

the_board = { 
    "top-L": ' ', "top-M": ' ', "top-R": ' ',
    "mid-L": ' ', "mid-M": ' ', "mid-R": ' ',
    "low-L": ' ', "low-M": ' ', "low-R": ' '}

def print_the_board():
    # This function prints the tic tac toe board
    print(f"{the_board['top-L']} | {the_board['top-M']} | {the_board['top-R']}")
    print("- + - + - " )
    print(f"{the_board['mid-L']} | {the_board['mid-M']} | {the_board['mid-R']}")
    print("- + - + - " )
    print(f"{the_board['low-L']} | {the_board['low-M']} | {the_board['low-R']}")

turn = 'X'

def find_winner():
    # this function evaluates the winner of a tictactoe game 
    if(not(the_board['top-L'] == ' ') and ((the_board['top-L'] == the_board['top-R']) and (the_board['top-R'] == the_board['top-L']))):
        print(f"{the_board['top-L']} wins") # causing issues so were gonna make a list out of this
        sys.exit()

while ' ' in the_board.values():
    print(f"It is {turn}'s turn")
    move = input("Enter a position to play at \n => ")
    # check if that position is still free
    if(the_board[move] == ' '): # when that position is free
        the_board[move] = turn
    else:
        print(f"{the_board[move]} has already played there. Choose a different position") # when the position has been played
        continue
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    print_the_board()
    find_winner()