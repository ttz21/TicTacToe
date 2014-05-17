print "Welcome to Tic Tac Toe, in order to play please enter your row and column numbers between 1 and 3"

import random


def print_board(board):
    for i in range(0,3):
        print " "+board[i][0]+" : "+board[i][1]+" : "+board[i][2]
        if i<=1:
            print "..........."



def get_player_input(player_name, coordinate):
    correct_input=False
    while(not correct_input):
        value = raw_input("Player "+player_name+", it is your go, enter your desired "+coordinate+": ")
 
        try:
            value=int(value)
        except ValueError:
            print "That is not a valid input!"
             
        if value>3 or value<1:
            print "Co-ordinate must be a number between 1 and 3"
        else:
            correct_input=True
    return value

def get_AI_input(player_name):
    correct_input=False
    while(not correct_input):
        row_value = random.randint(1,3)
        col_value = random.randint(1,3)
        if (valid_cell(board, row_value, col_value)):
            board[row_value-1][col_value-1]=player_name
            print_board(board)
            correct_input=True
            

def check_player_input(player_name):
    valid=False
    while(not valid):
        row_value = get_player_input(player_name,"row")
        col_value = get_player_input(player_name,"col")
 
        if(valid_cell(board, row_value, col_value)):
            board[row_value-1][col_value-1]=player_name
            print_board(board)
            valid=True
        else:
            print "That cell is already taken!"
                      

"""
Check win condition 
"""
def check_for_win(board, player_name):
    if (board[0][0]==board[1][1]==board[2][2]==player_name):
        return True
    if (board[0][2]==board[1][1]==board[2][0]==player_name):
        return True
    for i in range(0,3):
        if(board[i][0]==board[i][1]==board[i][2]==player_name):
            return True
        if(board[0][i]==board[1][i]==board[2][i]==player_name):
            return True
    return False
                                 


"""
Check if cell is empty
"""

def valid_cell(board, row_value, col_value):
    if(board[row_value-1][col_value-1]==" "):
        return True
    else:
        return False



"""
Check if board is full
"""

def board_full(board):
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==" ":
                return False

    return True




    
"""
Initialise board
"""

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
print_board(board)

"""
Alternate between players and loop until there is a winner...
"""

def determine_play_mode():
    mode = raw_input("Would you like a 1 or 2 player game? ")
    return mode #can also add code to take care of invalid inputs
 
def determine_first_go():
    go= raw_input("Who would like to go first? (X, O, or flip a coin?)")
    if(go.upper()=="X"):
        return["X", "O"]

    elif(go.upper()=="O"):
        return ["O", "X"]

    else:
        if(random.randint(0,1)==0):
            return ["O", "X"]
        else:
            return ["X", "O"]

    


gameplay = True
num_gos = 0

play_order = determine_first_go()
play_mode = determine_play_mode()

while gameplay:

    if(num_gos%2==0):
        check_player_input(play_order[0])

    else:
        if(play_mode == 2):
            check_player_input(play_order[1])
        else:
            print "Computer thinking..."
            get_AI_input(play_order[1])

    if(check_for_win(board,"X")):
        print "Congratulations Player X, you have won!"
        gameplay=False

    elif(check_for_win(board,"O")):
        print "Congratulations Player O, you have won!"
        gameplay=False

    elif(board_full(board)):
        print "This round was a draw..."
        gameplay=False

    if(not gameplay):
        again = raw_input("Would you like to play again? Enter Y to play again, or any other entry to quit: ")
        if (again.upper()=="Y"):
             gameplay = True
             board = [[" "," "," "],[" "," "," "],[" "," "," "]]
             play_order = determine_first_go()
             play_mode = determine_play_mode()
             num_gos=-1
              

    num_gos=num_gos+1
