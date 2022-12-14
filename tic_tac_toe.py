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

def store_values_in_list():
    parent_list = []
    values_list = list(the_board.values())

    for index in range(0, len(values_list), 3):
        row = values_list[index: index + 3]
        parent_list.append(row)
    
    return parent_list

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