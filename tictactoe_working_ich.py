#IS201 TicTacToe Group Project Assignment - Team C ("Team Sea")
#Ian, Celia, and Nathaniel

#
# FYI: The code below is Ian Hutcheson's initial solo attempt at a working game. 
# The team will be meeting in subsequent weeks to combine elements of each member's contributions.
# 
# 
#
# Worklist:
# - replace recursive loops (references to function from within that function) with logical loop iterations 
# - revise naming conventions to be universally understandable/descriptive
# - simplify dialog printed for user
#____________________________________

import random, time #import random and time functions

filename = 'tttlog.txt' #set filename for logging

#define values to display in middle of each graphic square
squares = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}    

#define nested dictionaries containing player attributes
players = {
    'player1': {
        'name': '', #player name, collected during setup
        'mode': '', #play mode, person vs comp
        'symbol': '', #player symbol, collected during setup
        'moves': [], #list of player moves this game
        },
    'player2': {
        'name': '',
        'mode': '',
        'symbol': '',
        'moves': [],
        },
    }

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9] #define list of available moves

order = [] #define blank list for later use in turn order

turn_log = [] #define blank list for turn logging

#draw board using values from squares dict
def print_board():
    """prints the game board"""
    print(f" _________________\n|     |     |     |\n|  {squares[1]}  |  {squares[2]}  |  {squares[3]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {squares[4]}  |  {squares[5]}  |  {squares[6]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {squares[7]}  |  {squares[8]}  |  {squares[9]}  |\n|_____|_____|_____|\n")
    next

#define lists of all possible winning move combinations
win1 = [1, 2, 3]
win2 = [4, 5, 6]
win3 = [7, 8, 9]
win4 = [1, 4, 7]
win5 = [2, 5, 8]
win6 = [3, 6, 9]
win7 = [1, 5, 9]
win8 = [7, 5, 3]

#nested lists containing winning combinations (for later use in turns when checking for win status)
winlist = [win1, win2, win3, win4, win5, win6, win7, win8]

qt = "'\033[1mq\033[0m' to \033[1mquit\033[0m...\n" #define variable qt for future print usage (leave function)

#define function to determine if user wants to play another person vs themselves
def get_mode():
    """has the user select which mode/opponent they'd like to play"""
    n = input(f"\t'\033[1m1\033[0m' to play against computer,\n\t'\033[1m2\033[0m' to play against another person, or \n\t{qt}") #prompt user for input
    leave(n) #check if user entered q to quit
    if n == '1': #if user entered 1, set up game for person vs computer
        players['player1']['mode'] = 'person' #set player 1 mode as person
        players['player2']['mode'] = 'computer' # set player 2 mode as computer
        players['player2']['name'] = 'tic tac toe bot 5000' #set player 2 name as bot
    elif n == '2': #check if user entered 2 to play other person
        player2() #collect 2nd player's name
    else: #fail loop for invalid input
        print(f"c'mon, {players['player1']['name'].title()}- you've got this.")
        get_mode() #re-run on invalid input

def player2(): #collect 2nd player's name if 2p selected
    """collect additional name, parameters if 2p mode is selected"""
    print("the more the merrier! who will you be playing with?") #solicit2nd name
    players['player1']['mode'] = 'person' #set player 1 mode
    players['player2']['mode'] = 'person' #set player 2 mode
    get_name() #invoke get_name function for 2nd player

def leave(n): #define function to quit game
    """allows user to leave the game"""
    if n == 'q': #check if input equals 'q'
        print("Okay, have a nice day!") #print farewell
        quit() #quit game

def get_name(): #define script to collect player name
    """collect p1's name"""
    n = input(f"\n\tplease enter a real human name or {qt}") #assign user input to variable n
    leave(n) #check if user chose to quit
    if len(n) == 0: #if user did not provide input...
        print(f"\n\t...no name? who doesn't have a name? \n\t\tok, come on No-Name, let's get a real name please!\n") #reprompt for name
        get_name() #call function again
    elif n.isdigit(): #check if user provided number
        print("\n\t...a number name?  let's get a real name please!\n") #prod user for correct input
        get_name() #call function again
    elif players['player1']['name'] != '': #check if player1's name is already assigned
        players['player2']['name'] = n #if YES, assign player2's name
        next #proceed
    else: #if player1 name not yet assigned..n
        players['player1']['name'] = n #assign player1 name
        next #proceed

def choose_sym(): #define function to choose player's symbol (x or o)
    """allow user to select preferred game symbol"""
    print(f"as i'm sure you know, {players['player1']['name'].title()}, 'X' always goes first in Tic-Tac-Toe. \n\t\twhich symbol would you like to be: '\033[1mX\033[0m' or '\033[1mO\033[0m'?\n") #adv. user of choice
    n = input(f"\tenter '\033[1mx\033[0m', '\033[1mo\033[0m', or {qt}") #prompt user to enter preferred symbol
    leave(n) #check if user chose to quit
    if n == 'x': #check if user chose 'x'
        print("you've chosen to play as 'X'! you will go first. your opponent will be 'O' and go second.") #confirm choice
        players['player1']['symbol'] = 'x' #set player symbols in players dictionary
        players['player2']['symbol'] = 'o' #set player symbols in players dictionary
        order.append('player1') #set turn order in order list
        order.append('player2') #set turn order in order list
    elif n == 'o': #check if user chose 'o'
        print("you've chosen to play as 'O'! you will go second. your opponent will be 'X' and will go first.") #confirm choice
        players['player1']['symbol'] = 'o' #set player symbols in players dictionary
        players['player2']['symbol'] = 'x' #set player symbols in players dictionary
        order.append('player2') #set turn order in order list
        order.append('player1') #set turn order in order list
    else: #handle invalid input
        print(f"were you the kid that didn't like following instructions growing up? c'mon, you've got this.") #adv user correct input needed
        choose_sym() #call function again
        next #proceed

def log(sym, mv): #define logging function
    """record choices throughout gameplay"""
    turn_log.append({ #for each turn, add the following items to turn_log dictionary:
        'turn': len(turn_log) + 1, #iterate turn number
        'sym': sym, # set symbol for move entry
        'mv': mv, #set square selected by symbol
    })

def write_log(): #define function to write turn_log content to log file 
    """at conclusion, write log of moves to local file"""
    with open(filename, 'w') as f: #set write permission with open file
        for t in turn_log: #loop for lines in turn_log dictionary
            f.write(f"Turn {t['turn']}: {t['sym']} selected {t['mv']}\n") #write each line in predefined format to log file


def bot_play(n): #define function for computer play when vs. comp mode is active
    """define logic for computer's turn in game"""
    print_board() #display game board
    if  moves: # check if moves are still available in list
        num = random.choice(moves) #have computer select a random available number
        players[n]['moves'].append(num) #add computer's move selection to player2 nested dictionary
        moves.remove(num) #remove selection from list of available moves
        print(f"{players[n]['name'].title()} selected {num}") #print confirmation of player's move selection
        squares[num] = players[n]['symbol'] #write player's move selection to squares dictionary
        log(players[n]['symbol'], num) #write user's turn to turn_log via log function
    else: #check if no moves left
        print("No moves left- STALEMATE!") #advise no moves left
        log('stalemate', 'stalemate') #write stalemate to list turn_log 
        write_log() #write turn_log to file
        quit() #quit program

def human_play(n): #define function for human turn (used in both 1p and 2p modes)
    """define logic for human's turn in game"""
    print_board() #print gameboard
    num = input(f"{players[n]['name'].title()}, select an available spot on the board (1-9) or {qt}:")#prompt user to enter move selection
    leave(n) #check if user opted to quit
    try: #exception handling for non-integer input
        num = int(num) #validate entry is number
    except ValueError: #handle ValueError gracefully
        print(f"Invalid input- please enter an available number between 1 and 9 or {qt}.")#adv of error
        human_play(n)#call function again
        return
    else: #if no ValueError:
        if num in moves: #check if user input is an available move in moves list
            squares[num] = players[n]['symbol'] #write player's symbol to squares dictionary
            players[n]['moves'].append(num) #add player's move to move list in their respective dictionary
            moves.remove(num) #remove user's move from list of available moves
            print(f"{players[n]['name'].title()} selected {num}") #print confirmation of move selection
            log(players[n]['symbol'], num) #write move to list turn_log
        else: #check if user entered move that is not in list of available moves
            print(f"{num} not available!\n\tselect an available spot on the board.") #adv move not available
            human_play(n) #call human_play function again

def win_check(): #define function to check if game has been won
    """check if game has been won"""
    for w in winlist: #loop through nested lists in winlist
        if all(num in players['player1']['moves'] for num in w): #check if all numbers in nested winlist appear in player's move list embedded in player1 dictionary
            return True #if match, return true
        elif all(num in players['player2']['moves'] for num in w): #check if all numbers in nested winlist appear in player's move list embedded in player2 dictionary
            return True #if match, return true
    return False #else, return false

def stale_check(): #check for stalemate
    for m in moves: # for remaining moves in list of available moves
        if moves == '': #if no remaining moves left
            print_board() #print game board
            print("No moves left- STALEMATE!") #advise no moves left
            log('stalemate', 'stalemate') #write stalemate to list turn_log 
            write_log() #write turn_log to file
            quit() #quit program
        else:
            next #proceed

def play(): #define function for advancing through gameplay
    while not win_check(): #proceed with loop as long as game has not been won
        stale_check() #perform stalemate check
        for n in order: #loop through player order in order list
            if players[n]['name'] == 'tic tac toe bot 5000': #if player name is TTTbot5k
                bot_play(n) #initiate bot_play function
            else: #if not bot
                human_play(n) #initiate human_play function
            if win_check() == True: #if win_check function finds a player has won
                print_board() #print game board
                print(f"game over! {players[n]['name'].title()} is the winner.") #adv. game is over
                write_log() #write turn_log to file
                quit() #quit program
            time.sleep(2) #sleep for two seconds

def ready_up(): #define function to check if player is ready to play
    n = input(f"\tenter '\033[my\033[0m' to play or {qt}") #prompt user to input y to play or q to quit, then assign input to 'n' variable
    if n == 'y': #if input is y
        play() #call play function
    elif n == 'q': #if input is q
        leave(n)  #call quit function
    else: #otherwise,
        print(f"were you the kid that didn't like following instructions growing up? c'mon, you've got this.") #prompt user to enter valid input
        ready_up() #re-run ready_up function

print(f"hi! welcome to Tic-Tac-Toe.") #print initial greeting
print(f"\nwhat is your \033[1mname\033[0m?") #print initial greeting
get_name() #run function to collect player1 name from user

print(f"\nvery good- hello {players['player1']['name'].title()}! \n\tnow, would you like to play against...") #print message confirming player1 name
print("\t\t\033[1mME\033[0m (TicTacToeBot 5000, beep bopp boop!)?") #print message asking if player would like to play against computer
print("\t\t\tor...") #or
print("\t\tanother \033[1mPERSON\033[0m?") #print message if player would like to play against another person

get_mode() #call get_mode function to determine if player wants to play computer or person
choose_sym() #call function to determine if player wants to play as 'x' or 'o'

#print summary of selections
print(f"summary:\n\n{players['player1']['name'].title()}               {players['player2']['name'].title()}")
print(f"{players['player1']['mode']}     vs.    {players['player2']['mode']}")
print(f"{players['player1']['symbol']}                 {players['player2']['symbol']}")
print(f"\nready to play?\n") #print message asking if player is ready to enter game
ready_up() #call ready_up function to start game

print_board() #print initial game board
play() #initiate gameplay