import random, time #import random and time functions

#set global variables
filename = 'tttlog.txt' #set filename for logging
bot_name = 'TicTacToeBot 5000'
squares = {i: str(i) for i in range(1, 10)} #define values to display in middle of each graphic square
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9] #define list of available moves
order = [] #define blank list for later use in turn order
turn_log = [] #define blank list for turn logging
bold = "\033[1m"
unbold = "\033[0m"
prompt_for_quit = f"'{bold}q{unbold}' to {bold}quit{unbold}...\n" #define variable qt for future print usage (quit_if_instructed function)

#nested lists containing winning combinations (for later use in turns when checking for win status)
winlist = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3]
]

class Player:
    def __init__(self, name='', mode='', symbol='', moves=None):
        if moves is None:
            moves = []
        self.name = name
        self.mode = mode
        self.symbol = symbol
        self.moves = moves

player1 = Player()  # define player 1
player2 = Player()  # define player 2

#draw board using values from squares dict
def print_board():
    """prints the game board"""
    print(  f" _________________\n|     |     |     |\n"
          + f"|  {squares[1]}  |  {squares[2]}  |  {squares[3]}  |\n"
          + f"|_____|_____|_____|\n|     |     |     |\n"
          + f"|  {squares[4]}  |  {squares[5]}  |  {squares[6]}  |\n"
          + f"|_____|_____|_____|\n|     |     |     |\n"
          + f"|  {squares[7]}  |  {squares[8]}  |  {squares[9]}  |\n"
          + f"|_____|_____|_____|\n")

def prompt_for_input(prompt): #define function to prompt user for input
    n = input(prompt) #assign user input to variable n
    n_lower = str.lower(n or "") #convert input to lowercase
    quit_if_instructed(n_lower) #check if user chose to quit
    return n_lower #return lowercase input

#define function to determine if user wants to play another person vs themselves
def get_mode():
    while 1 :
        """has the user select which mode/opponent they'd like to play"""
        n = prompt_for_input(f"\t'{bold}1{unbold}' to play against computer,\n\t'{bold}2{unbold}' to play against another person, or \n\t{prompt_for_quit}") #prompt user for input
        if n == '1': #if user entered 1, set up game for person vs computer
            player1.mode = 'person' #set player 1 mode as person
            player2.mode = 'computer' # set player 2 mode as computer
            player2.name = bot_name #set player 2 name as bot
            break
        elif n == '2': #check if user entered 2 to play other person
            print("the more the merrier! who will you be playing with?") #solicit2nd name
            player1.mode = 'person' #set player 1 mode
            player2.mode = 'person' #set player 2 mode
            player2.name = prompt_for_name() #invoke get_name function for 2nd player
            break
        else: #fail loop for invalid input
            print(f"c'mon, {player1.name.title()}- you've got this.")

def quit_if_instructed(n): #define function to quit game
    """allows user to quit_if_instructed the game"""
    if str.lower(n or "") == 'q': #check if input equals 'q'
        print("Okay, have a nice day!") #print farewell
        quit() #quit game

def prompt_for_name(): #define script to collect player name
    """collect a player's name"""
    while 1:
        n = prompt_for_input(f"\n\tplease enter a real human name or {prompt_for_quit}") #assign user input to variable n
        if len(n) == 0: #if user did not provide input...
            print(f"\n\t...no name? who doesn't have a name? \n\t\tok, come on No-Name, let's get a real name please!\n") #reprompt for name
        elif n.isdigit(): #check if user provided number
            print("\n\t...a number name?  let's get a real name please!\n") #prod user for correct input
        else:
            return n #return name to main script

def choose_sym(): #define function to choose player's symbol (x or o)
    """allow user to select preferred game symbol"""
    while 1:
        print(f"as i'm sure you know, {player1.name.title()}, 'X' always goes first in Tic-Tac-Toe. \n\t\twhich symbol would you like to be: '{bold}X{unbold}' or '{bold}O{unbold}'?\n") #adv. user of choice
        n = prompt_for_input(f"\tenter '{bold}x{unbold}', '{bold}o{unbold}', or {prompt_for_quit}") #prompt user to enter preferred symbol
        global order #set order as global variable
        if n == 'x': #check if user chose 'x'
            print("you've chosen to play as 'X'! you will go first. your opponent will be 'O' and go second.") #confirm choice
            player1.symbol = 'x' #set player symbols in players dictionary
            player2.symbol = 'o' #set player symbols in players dictionary
            order = [player1, player2]
            break
        elif n == 'o': #check if user chose 'o'
            print("you've chosen to play as 'O'! you will go second. your opponent will be 'X' and will go first.") #confirm choice
            player1.symbol = 'o' #set player symbols in players dictionary
            player2.symbol = 'x' #set player symbols in players dictionary
            order = [player2, player1]
            break
        else: #handle invalid input
            print(f"were you the kid that didn't like following instructions growing up? c'mon, you've got this.") #adv user correct input needed

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

def prompt_for_move(player): #define function to prompt user for move selection
    """prompt user for move selection"""
    if (player.name == bot_name): #check if player name is TTTbot5k
        return random.choice(moves) #have computer select a random available number
    while 1: #loop for user input
        num = prompt_for_input(f"{player.name.title()}, select an available spot on the board (1-9) or {prompt_for_quit}:") #prompt user to enter move selection
        try: #exception handling for non-integer input
            num = int(num) #validate entry is number
        except ValueError: #handle ValueError gracefully
            print(f"Invalid input- please enter an available number between 1 and 9 or {prompt_for_quit}.") #adv of error
        if num not in moves: #check if user entered move that is not in list of available moves
            print(f"{num} not available!\n\tselect an available spot on the board.") #adv move not available
        else: #if move is available
            return num

def take_turn(player): #define function for taking turns
    """define logic for taking turns in game"""
    print_board() #print game board
    num = prompt_for_move(player) #prompt user for move selection
    print(f"{player.name.title()} selected {num}") #print confirmation of move selection
    squares[num] = player.symbol #write player's symbol to squares dictionary
    player.moves.append(num) #add player's move to move list in their respective dictionary
    moves.remove(num) #remove user's move from list of available moves
    log(player.symbol, num) #write move to list turn_log

def win_check(): #define function to check if game has been won
    """check if game has been won"""
    for w in winlist: #loop through nested lists in winlist
        if all(num in player1.moves for num in w): #check if all numbers in nested winlist appear in player's move list embedded in player1 dictionary
            return True #if match, return true
        elif all(num in player2.moves for num in w): #check if all numbers in nested winlist appear in player's move list embedded in player2 dictionary
            return True #if match, return true
    return False #else, return false

def stale_check(): #check for stalemate
    if moves == '': #if no remaining moves left
        print_board() #print game board
        print("No moves left- STALEMATE!") #advise no moves left
        log('stalemate', 'stalemate') #write stalemate to list turn_log 
        write_log() #write turn_log to file
        quit() #quit program

def play(): #define function for advancing through gameplay
    while not win_check(): #proceed with loop as long as game has not been won
        stale_check() #perform stalemate check
        for player in order: #loop through player order in order list
            take_turn(player) #call take_turn function
            if win_check() == True: #if win_check function finds a player has won
                print_board() #print game board
                print(f"game over! {player.name.title()} is the winner.") #adv. game is over
                write_log() #write turn_log to file
                quit() #quit program
            time.sleep(1) #sleep for one seconds

def ready_up(): #define function to check if player is ready to play
    while 1: #loop for user input
        n = prompt_for_input(f"\tenter '{bold}y{unbold}' to play or {prompt_for_quit}") #prompt user to input y to play or q to quit, then assign input to 'n' variable
        if n == 'y': #if input is y
            return True
        else: #otherwise,
            print(f"were you the kid that didn't like following instructions growing up? c'mon, you've got this.") #prompt user to enter valid input

print(f"hi! welcome to Tic-Tac-Toe.") #print initial greeting
print(f"\nwhat is your {bold}name{unbold}?") #print initial greeting
player1.name = prompt_for_name() #run function to collect player1 name from user

print(f"\nvery good- hello {player1.name.title()}! \n\tnow, would you like to play against...") #print message confirming player1 name
print(f"\t\t{bold}ME{unbold} ({bot_name}, beep bopp boop!)?") #print message asking if player would like to play against computer
print(f"\t\t\tor...") #or
print(f"\t\tanother {bold}PERSON{unbold}?") #print message if player would like to play against another person

get_mode() #call get_mode function to determine if player wants to play computer or person
choose_sym() #call function to determine if player wants to play as 'x' or 'o'

#print summary of selections
vs = "vs. "
leftColWidth = max(len(player1.name), len(player1.mode)) + 2
print(f"summary:\n\n{player1.name.title().ljust(leftColWidth + len(vs))}{player2.name.title()}")
print(f"{player1.mode.ljust(leftColWidth)}{vs}{player2.mode}")
print(f"{player1.symbol.ljust(leftColWidth + len(vs))}{player2.symbol}")
print(f"\nready to play?\n") #print message asking if player is ready to enter game
if ready_up(): #call ready_up function to start game
    print_board() #print initial game board
    play() #initiate gameplay
