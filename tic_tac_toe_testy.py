#Define global variables
game_board = ['~','~','~','~','~','~','~','~','~']

player_1 = None
player_2 = None

game_active = True

active_player = None


#start function
def start_function():
     print('How about a round of Tic-Tac-Toe?')
     start = input('Hit any key to start.')
     if start != None:
        game_active == True


#print board game
def print_game_board(game_board):
    print(' | ' + '  ' + game_board[0] + '  ' + ' | ' + '  ' + game_board[1] + '  ' + ' | ' + '  ' + game_board[2] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[3] + '  ' + ' | ' + '  ' + game_board[4] + '  ' + ' | ' + '  ' + game_board[5] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[6] + '  ' + ' | ' + '  ' + game_board[7] + '  ' + ' | ' + '  ' + game_board[8] + '  ' + ' | ' )


#assigning symbols to player
def symbol_func(print):
    print("Welcome to a new round of Tic Tac Toe")
    player_1 = (input("Player 1 Please choose your Symbol, X or O: "))
    if player_1 == "X" or player_1 == "x":
        player_2 = "O" 
    else:
        player_2 = "X"
    print(f'Player 1 chose "{player_1}" and Player 2 chose "{player_2}"')
    #print(f'Player 1 chose "{player_1}" so Player 2 becomes "{player_2}"')


#Declaring active player
def declare_active_player(player_1):
    active_player = player_1
    print(active_player)


#Switch Active Player
def switch_active_player():
    active_player = player_2
    print(active_player)


#move player
def move_player(active_player):
    idx = int(input(f'{active_player}, Please input value 1 - 9 for the corresponding field in the game board:'))
    idx = idx-1
    game_board[idx] = active_player
    print_game_board(game_board)


#check win horizontal
def check_win_horizontal(game_board, active_player):
    if game_board[0] == game_board[1] == game_board[2] == active_player or game_board[3] == game_board[4] == game_board[5] == active_player or game_board[6] == game_board[7] == game_board[8] == active_player:
        print(f'{active_player} won!')
        game_active = False
    else:
        game_active = True


#check win vertical
def check_win_vertical(game_board, active_player):
    if game_board[0] == game_board[3] == game_board[6] == active_player or game_board[1] == game_board[4] == game_board[7] == active_player or game_board[2] == game_board[5] == game_board[8] == active_player:
        print(f'{active_player} won!')
        game_active = False
    else:
        game_active = True


#check win diagonal
def check_win_vertical(game_board, active_player):
    if game_board[0] == game_board[4] == game_board[8] == active_player or game_board[2] == game_board[4] == game_board[6] == active_player:
        print(f'{active_player} won!')
        game_active = False
    else:
        game_active = True


#check draw
def check_draw(game_board):
    for element in game_board:
        if '~' not in game_board:
            print("It's a Draw!")
            game_active = False
        else:
            game_active = True


#while loop to start all functions
#while game_active:
if __name__ == "__main__":
    start_function()
    print_game_board(game_board)
    symbol_func(print)
    declare_active_player(player_1)
    switch_active_player()
    move_player(active_player)
    check_win_horizontal(game_board, active_player)
    check_win_vertical(game_board, active_player)
    check_draw(game_board)

    
    


    
    
    