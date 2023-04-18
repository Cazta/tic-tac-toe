# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)


'''
*************************** initialize global variables ***************************************

# define global variables: '''

game_board = ['  ~  ','  ~  ','  ~  ','  ~  ','  ~  ','  ~  ','  ~  ','  ~  ','  ~  ']

player_1 = None
player_2 = None

game_active = True

'''
**************************** starting game message **************************************

# Commandline to start the Game from terminal?

'''
def start_function():
     print('How about a round of Tic-Tac-Toe?')
     start = input('Hit any key to start.')
     if start != None:
          global game_active
          game_active == True

'''
**************************** Greeting, and chose symbol player 1, assign symbol player 2 **************************************
def start_func():

    print ("Welcome to a new round of Tic Tac Toe")

    player_1 = input("Player 1 Please choose your Symbol, X or O")

       # if player_1 = X:
        #    player_2 = O
                # print("Player 1 chose X or O and Player 2 chose O or X, Now the Game begins, get ready!")
        # else:
             player_2 = X
                # print("Player 1 chose X or O and Player 2 chose O or X, Now the Game begins, get ready!")

'''
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

        






'''***************************** print game board *************************************

# def print_game_board
    # game_board = list [ ' ',' ',' ',' ',' ',' ',' ',' ',' ']
        # print line 1 = game_board[0:2]
        # print line 2 = game_board[1]
        # print line 3 = game_board[2]

        # print('help')'''

def print_game_board(game_board):
    print(' | ' + game_board[0] + ' | ' + game_board[1] + ' | ' + game_board[2] + ' | ' )
    print('---------------------------')
    print(' | ' + game_board[3] + ' | ' + game_board[4] + ' | ' + game_board[5] + ' | ' )
    print('---------------------------')
    print(' | ' + game_board[6] + ' | ' + game_board[7] + ' | ' + game_board[8] + ' | ' )


***************************** move player 1 *************************************        

# def move_player_1 int(input) if possible with message: ("Player 1 please input value 1-9 for corresponding field in mage board:")
    # for-loop to replace item in game_board with player_1(=x or 0)
        #for i in range(len(game_board)):
            #if board_game[input-1] == input:
                #board_game[input-1] = player_1
                    #print(game_board)
            #else:
                #print('invalid game board field, try again')
                    #continue

***************************** check for win after move player 1 *************************************  

# def check_win_player_1:
    if game_board[0][0:2] == player_1:
            print(win message player_1, player_2 is a loser)

    repeat until end (board_game[2][2]
        with 8 winning possiblities!!!

        if win condition is met:
            game_active = False

******************************* check for draw after move player 1 ***********************************
        
def check_draw:
    for i in game_board:
        if ' ' not in game_board:
            print('draw message')
                break out of the game
        else:
            break

******************************** move player 2 **********************************
            
# def move_player_2 int(input) if possible with message: ("Player 2 please input value 1-9 for corresponding field in mage board:")
    # for-loop to replace item in game_board with player_2(=x or 0)
        #for i in range(len(game_board)):
            #if board_game[input-1] == input:
                #board_game[input-1] = player_2
                    #print(game_board)
            #else:
                #print('invalid game board field, try again')
                    #continue

***************************** check for win after move player 2 *************************************  
                    
# def check_win_player_2:
    if game_board[0][0:2] == player_2:
            print(win message player_2, player_1 is a loser)
                break out of the game

    repeat until end (board_game[2][2]
        with 8 winning possiblities!!!                   

        if win condition is met:
            game_active = False
        


******************************************************************

maybe func to end the game and suggest a new round?




******************************************************************








other option, may not use!

    # Store index of chosen field in variable move_index
        # if input =! rage(1:10)
            # print ("Player 1 entered a invalid field")
            # continue
        # elif: (Checking if the field is already taken, but how?)
            # if input = 1:
                #game_board[0][0]
                    # if game_board[0][0] = X or game_board[0][0] = O:
                        # print("This field is already taken, choose a free one!")
            # continue
        # else:
            # game_board[0][0] = player_1
        # repeat (copy/paste) till input = 9

        
'''





# Function for ... (displaying the board?)
def blabla():
    pass


# Function for... (choosing a player?)
def blablabla():
    pass


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
