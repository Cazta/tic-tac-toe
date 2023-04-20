import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#Define global variables
game_board = ['~','~','~','~','~','~','~','~','~']

player_1 = None
player_2 = None
win = None
game_active = True



#start function
def start_function():
     print()
     print(Fore.CYAN + "***********************************\n*How about a round of Tic-Tac-Toe?*\n***********************************")
     print()
     start = input(Fore.MAGENTA + 'Hit any key to start.')
     if start != None:
        game_active = True
              

#assigning symbols to player
def symbol_func():
    print()
    print(Fore.CYAN + "***************************************\n*Welcome to a new round of Tic Tac Toe*\n***************************************")
    print()
    global player_1 
    global player_2
    print()
    player_1 = (input("Player 1 Please choose your Symbol, X or O: ")) 
    if player_1 == "X" or player_1 == "x":
        player_1 = "X"
        player_2 = "O"
        print()
        print(f'Player 1 chose "{player_1}" so Player 2 is "{player_2}"')
        print()
    elif player_1 == "O" or player_1 == "o":
        player_1 = "O"
        player_2 = "X"
        print()
        print(f'Player 1 chose "{player_1}" so Player 2 is "{player_2}"')
        print()
    elif player_1 != "X" or player_1 != "x" or player_1 != "O" or player_1 != "o":
        print()
        print('\033[31m'+'You must enter either X or O')
        print('\033[39m')
        print()
        symbol_func()
    print_game_board(game_board)


#print board game
def print_game_board(game_board):
    print()
    print(' | ' + '  ' + game_board[0] + '  ' + ' | ' + '  ' + game_board[1] + '  ' + ' | ' + '  ' + game_board[2] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[3] + '  ' + ' | ' + '  ' + game_board[4] + '  ' + ' | ' + '  ' + game_board[5] + '  ' + ' | ' )
    print('---------------------------')
    print(' | ' + '  ' + game_board[6] + '  ' + ' | ' + '  ' + game_board[7] + '  ' + ' | ' + '  ' + game_board[8] + '  ' + ' | ' )
    print()

#Declaring active player
def declare_active_player(player_1):
    global active_player
    active_player = player_1
    return active_player

#move player
def move_player(active_player):
    print()
    idx = int(input(f'{active_player}, please input value 1 - 9 for the corresponding field in game board:'))
    idx = idx-1
#if input field outside of game board, print error message, prompt for another input
    if idx not in range(0,9):
        print()
        print('\033[31m'+'Whoopsie-daisy, field not in game board. Try again')
        print('\033[39m')
        print()
        move_player(active_player)
#if input field is already occupied, print error message, prompt for another input
    elif game_board[idx] != '~':
        print()
        print('\033[31m'+'Whoopsie-daisy, field already occupied. Try again')
        print('\033[39m')
        print()
        move_player(active_player)
#for valid input, set symbol into game board
    else: 
        game_board[idx] = active_player
        print()
        print_game_board(game_board)


#check winning conditions
def check_win(game_board, active_player):
    global win
    if game_board[0] == game_board[1] == game_board[2] == active_player or game_board[3] == game_board[4] == game_board[5] == active_player or game_board[6] == game_board[7] == game_board[8] == active_player:
        win = 1
        print()
        print(f'{active_player} won!')
    #check win vertical
    elif game_board[0] == game_board[3] == game_board[6] == active_player or game_board[1] == game_board[4] == game_board[7] == active_player or game_board[2] == game_board[5] == game_board[8] == active_player: 
        win = 1
        print()
        print(f'{active_player} won!')
    #check win diagonal
    elif game_board[0] == game_board[4] == game_board[8] == active_player or game_board[2] == game_board[4] == game_board[6] == active_player:
        win = 1
        print()
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
        print()
        print("It's a Draw! Try another round!")
        print()
    return draw

#Switch Active Player
def switch_active_player():
    global active_player
    if active_player == player_1:
        active_player = player_2
    elif active_player == player_2:
        active_player = player_1

#Ask for another round
#def another_round():



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
  

    
    


    
    
    