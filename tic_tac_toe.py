import sys, copy

the_board = { 
    "top-L": ' ', "top-M": ' ', "top-R": ' ',
    "mid-L": ' ', "mid-M": ' ', "mid-R": ' ',
    "low-L": ' ', "low-M": ' ', "low-R": ' '
}

counter = 0
x_wins = 0
o_wins = 0

def print_the_board():
    # This function prints the tic tac toe board

    print(f"{the_board['top-L']} | {the_board['top-M']} | {the_board['top-R']}")
    print("- + - + - " )
    print(f"{the_board['mid-L']} | {the_board['mid-M']} | {the_board['mid-R']}")
    print("- + - + - " )
    print(f"{the_board['low-L']} | {the_board['low-M']} | {the_board['low-R']}")

def store_values_in_list():
    # This function changed the dictionary to a 2 dimensional list with 3 items in each list

    parent_list = []
    values_list = list(the_board.values())

    for index in range(0, len(values_list), 3):
        row = values_list[index: index + 3]
        parent_list.append(row)
    
    return parent_list

def find_winner():
    # This functin evaluates who won the game
    winner = ''
    values_list = store_values_in_list()

    for x in range(3):
        for y in range(3):
            right = (y + 1) % 3
            dbl_right = (y + 2) % 3
            left = (y - 1) % 3
            dbl_left = (y - 2) % 3
            top = (x - 1) % 3
            dbl_top = (x - 2) % 3
            down = (x + 1) % 3
            dbl_down = (x + 2) % 3

            if(not(values_list[x][y] == ' ')):
                if(values_list[x][y] == values_list[x][right] == values_list[x][dbl_right]):
                    print(f"\n{values_list[x][y]} wins\n") # formed a horizontal line
                    return [True, values_list[x][y]]
                if(values_list[x][y] == values_list[down][y] == values_list[dbl_down][y]):
                    print(f"\n{values_list[x][y]} wins\n") # formed a vertical line
                    return [True, values_list[x][y]]
                if((values_list[0][0] == values_list[1][1] == values_list[2][2]) and not(values_list[1][1] == ' ')):
                    print(f"\n{values_list[1][1]} wins\n") # formed a right diagonal
                    return [True, values_list[1][1]]
                if(values_list[0][2] == values_list[1][1] == values_list[2][0] and not(values_list[1][1] == ' ')):
                    print(f"\n{values_list[1][1]} wins\n") # formed a left diagonal
                    return [True, values_list[1][1]]
                if(' ' not in the_board.values()):
                    return [False, None]

def reset_the_board():
    # This function removes all the items in the board

    global the_board
    the_board = { 
    "top-L": ' ', "top-M": ' ', "top-R": ' ',
    "mid-L": ' ', "mid-M": ' ', "mid-R": ' ',
    "low-L": ' ', "low-M": ' ', "low-R": ' '
}


while True:
    print('New Board')
    if(counter % 2 == 0):
        turn = 'X'
    else:
        turn = 'O'

    if(counter == 3):
        break

    while True:
        print(f"It is {turn}'s turn. (Enter 'q' to quit)")
        move = input("Enter a position to play at \n => ")

        # check if that position is still free

        try:
            if(the_board[move] == ' '): # when that position is free
                the_board[move] = turn
            else:
                print(f"{the_board[move]} has already played there. Choose a different position") # when the position has been played
                continue
        except KeyError:
            print("Sorry that position doesn't exist. Try low, top and mid with -R, -L or -M")
            continue
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        print_the_board()
        winner_list = copy.copy(find_winner())

        if(winner_list != None):
            if((winner_list[0] == True) and (winner_list[1] == 'X')):
                x_wins += 1
            elif((winner_list[0] == True) and (winner_list[1] == 'O')):
                o_wins += 1
            elif(winner_list[0] == False):
                print("\nIt's a tie👔\n")
            reset_the_board()
            break
            
    counter += 1

print(f"GAME OVER!\nX - O\n{x_wins} - {o_wins}")