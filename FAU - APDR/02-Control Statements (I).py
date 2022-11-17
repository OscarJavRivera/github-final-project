## While playing tic-tac-toe you need to set the next player ##
## There can be two players in tic-tac-toe. One is 'X' and the other is 'O' ##
## If current player is 'X' then set the player for the next move as 'O' and vice versa ##
def next_player(current_player):
    '''(str) --> (str)
    Returns the next player given the current_player.
    '''

    ## Specify the conditional if else statements to change the player ##
    ## Store the next player value in the variable current_player itself ##
    #TODO: Write your code below

    if current_player == 'X' :
        current_player='O'
        
    elif current_player=='O':
        current_player='X'
    else:
        current_player==''
        print("Wrong Input")
    
    print ("This is the next player",current_player)
    return current_player

next_player('X')
next_player('O')
board=['X','X','X','O','O','O','O','O','O']

def check_win(board , current_player):
    '''(dict,str) --> (bool)
    Return True if current_player has won the game.
    '''

    ## Specify the conditional if else statements to check if player current_player has won ##
    ## To check what is the value in position 1 of the board you can use the following: board[1]. ##
    ## Use this to make up your conditional statements. ##
    # TODO: Complete the if else conditions. The starting if and the ending else statement is given.
    #  Take inspiration from them to complete your task

    if current_player in board[1] and current_player in board[2] and current_player in board[3]: ##1,2,3
        return True
    elif current_player in board[1] and current_player in board[4] and current_player in board[7]: ##1,4,7
        return True
    elif current_player in board[1] and current_player in board[5] and current_player in board[9]: ##1,5,9
        return True
    elif current_player in board[2] and current_player in board[5] and current_player in board[8]: ##2,5,8
        return True
    elif current_player in board[3] and current_player in board[6] and current_player in board[9]: ##3,6,9
        return True
    elif current_player in board[3] and current_player in board[5] and current_player in board[7]: ##3,5,7
        return True
    elif current_player in board[4] and current_player in board[5] and current_player in board[6]: ##4,5,6
        return True
    elif current_player in board[7] and current_player in board[8] and current_player in board[9]: ##7,8,9
        return True
    else:
        return False

def check_draw(num_moves):
    '''(int) --> (bool)
    Return True or False given the total number of moves played given by num_moves.
    '''

    ## Specify the conditional if else statements to check if the game is a draw ##
    # TODO: Write the if condition to check if the match is not a draw yet.

    if num_moves==5:
        return False
    else:
        return True
