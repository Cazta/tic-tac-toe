#Define global variables
game_board = ['~','~','~','~','~','~','~','~','~']

global player_1
global player_2

global game_active

active_player = None



#start function
def start_function():
     print('How about a round of Tic-Tac-Toe?')
     start = input('Hit any key to start.')
     if start != None:
        game_active = True
              

#assigning symbols to player
def symbol_func():
    print("Welcome to a new round of Tic Tac Toe")
    #global player_1 
    active_player = (input("Player 1 Please choose your Symbol, X or O: "))
    #global player_2 
    if active_player == "X" or active_player == "x":
        player_2 = "O" 
    else:
        player_2 = "X"
    print(f'Player 1 chose "{active_player}" and Player 2 chose "{player_2}"')

#print board game
def print_game_board(game_board):
    print(' | ' + '  ' + game_board[0] + '  ' + ' | ' + '  ' + game_board[1] + '  ' + ' | ' + '  ' + game_board[2] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[3] + '  ' + ' | ' + '  ' + game_board[4] + '  ' + ' | ' + '  ' + game_board[5] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[6] + '  ' + ' | ' + '  ' + game_board[7] + '  ' + ' | ' + '  ' + game_board[8] + '  ' + ' | ' )

'''  #Declaring active player
def declare_active_player(player_1):
    #global active_player
    active_player = player_1'''

#move player
def move_player(active_player):
    idx = int(input(f'{active_player}, please input value 1 - 9 for the corresponding field in game board:'))
    idx = idx-1
    game_board[idx] = active_player
    print_game_board(game_board)


#check win horizontal
def check_win_horizontal(game_board, active_player):
    if game_board[0] == game_board[1] == game_board[2] == active_player or game_board[3] == game_board[4] == game_board[5] == active_player or game_board[6] == game_board[7] == game_board[8] == active_player:
        print(f'{active_player} won!')
        #global game_active
        game_active = False
    else:
        game_active = True


#check win vertical
def check_win_vertical(game_board, active_player):
    if game_board[0] == game_board[3] == game_board[6] == active_player or game_board[1] == game_board[4] == game_board[7] == active_player or game_board[2] == game_board[5] == game_board[8] == active_player:
        print(f'{active_player} won!')
        #global game_active
        game_active = False
    else:
        game_active = True


#check win diagonal
def check_win_diagonal(game_board, active_player):
    if game_board[0] == game_board[4] == game_board[8] == active_player or game_board[2] == game_board[4] == game_board[6] == active_player:
        print(f'{active_player} won!')
        #global game_active
        game_active = False
    else:
        game_active = True


#check draw
def check_draw(game_board):
    #global game_active
    if '~' not in game_board:
        game_active = False
    else:
        game_active = True
    if game_active == False:
        print("It's a Draw!")



#Switch Active Player
def switch_active_player():
    #global active_player
    if active_player == player_1:
        active_player = player_2
    elif active_player == player_2:
        active_player = player_1



#while loop to start all functions
def play_game():
    start_function()
    symbol_func()
    #declare_active_player(player_1)
    game_active = True
    while game_active == True:
        move_player(active_player)
        check_win_horizontal(game_board, active_player)
        check_win_vertical(game_board, active_player)
        check_win_diagonal(game_board, active_player)
        check_draw(game_board)
        switch_active_player()
    else:
        print("The game is over!")
        

play_game()
  

    
    


    
    
    