#Define global variables
game_board = ['~','~','~','~','~','~','~','~','~']

player_1 = None
player_2 = None
win = None
game_active = True



#start function
def start_function():
     print('How about a round of Tic-Tac-Toe?')
     start = input('Hit any key to start.')
     if start != None:
        game_active = True
              

#assigning symbols to player
def symbol_func():
    print("Welcome to a new round of Tic Tac Toe")
    global player_1 
    player_1 = (input("Player 1 Please choose your Symbol, X or O: "))
    global player_2 
    if player_1 == "X" or player_1 == "x":
        player_2 = "O" 
    else:
        player_2 = "X"
    print(f'Player 1 chose "{player_1}" and Player 2 chose "{player_2}"')
    print_game_board(game_board)


#print board game
def print_game_board(game_board):
    print(' | ' + '  ' + game_board[0] + '  ' + ' | ' + '  ' + game_board[1] + '  ' + ' | ' + '  ' + game_board[2] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[3] + '  ' + ' | ' + '  ' + game_board[4] + '  ' + ' | ' + '  ' + game_board[5] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[6] + '  ' + ' | ' + '  ' + game_board[7] + '  ' + ' | ' + '  ' + game_board[8] + '  ' + ' | ' )

#Declaring active player
def declare_active_player(player_1):
    global active_player
    active_player = player_1
    return active_player

#move player
def move_player(active_player):
    idx = int(input(f'{active_player}, please input value 1 - 9 for the corresponding field in game board:'))
    idx = idx-1
#if input field outside of game board, print error message, prompt for another input
    if idx not in range(0,9):
        print('Whoopsie-daisy, field not in game board. Try again')
        move_player(active_player)
#if input field is already occupied, print error message, prompt for another input
    elif game_board[idx] != '~':
        print('Whoopsie-daisy, field already occupied. Try again')
        move_player(active_player)
#for valid input, set symbol into game board
    else: 
        game_board[idx] = active_player
        print_game_board(game_board)


#check winning conditions
def check_win(game_board, active_player):
    global win
    if game_board[0] == game_board[1] == game_board[2] == active_player or game_board[3] == game_board[4] == game_board[5] == active_player or game_board[6] == game_board[7] == game_board[8] == active_player:
        win = 1
        print(f'{active_player} won!')
    #check win vertical
    elif game_board[0] == game_board[3] == game_board[6] == active_player or game_board[1] == game_board[4] == game_board[7] == active_player or game_board[2] == game_board[5] == game_board[8] == active_player: 
        win = 1
        print(f'{active_player} won!')
    #check win diagonal
    elif game_board[0] == game_board[4] == game_board[8] == active_player or game_board[2] == game_board[4] == game_board[6] == active_player:
        win = 1
        print(f'{active_player} won!')
    else:
        win = 0  
    return win
    #return game_active


#check draw
def check_draw(game_board):
    global draw
    if '~' not in game_board and win != 1:
        draw = 1
    else:
        draw = 0
    if draw == 1:
        print("It's a Draw! Try another round!")
    return draw

#Switch Active Player
def switch_active_player():
    global active_player
    if active_player == player_1:
        active_player = player_2
    elif active_player == player_2:
        active_player = player_1


#while loop to start all functions
def play_game():
    start_function()
    symbol_func()
    declare_active_player(player_1)
    game_active = True
    while game_active:
        move_player(active_player)
        check_win(game_board, active_player)
        #check_win_vertical(game_board, active_player)
        #check_win_diagonal(game_board, active_player)
        check_draw(game_board)
        if win == 1:
            game_active = False
            print('Thank you for playing!')
        elif draw == 1:
            game_active = False
        else:
            switch_active_player()



play_game()
  

    
    


    
    
    