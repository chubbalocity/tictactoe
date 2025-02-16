#tictactoe personal main

### Team Sea ###
#     (..)     #
#   (((())))   #
################
# Celia Chesebro 
# Ian Hutcheson
# Nathaniel Mcrae

# greeting
# ask 1 or 2 players - skipping for now
# ask X or O - x goes first
# if X playerX
# if O playerO
# O is computer if not person

### IMPORTS
import random # used in greeting, first move if computer
import sys # used to exit when quit is given as input

#fix print opening credits centered.
OpCreditText= """
### TEAM SEA ###
#     (..)     #
#   (((())))   #
####PRESENTS####
##TIC#TAC#TOE###
"""
#    -------------
#    | A | B | C |
#    -------------
#    | D | E | F |
#    -------------
#    | G | H | I |
#    -------------
###Your program saves all the moves between players in a file called tictactoe.txt

# Board Dictionary
TTTBoard = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I"}
Centerwidth = 60 

# salutation
#needs import random
def salutation():
   Greeting = ["Hey", "Hi", "Hello"]
   Salutation = Greeting[random.randint(0, len(Greeting) - 1)]
   print(Salutation, "there! Let's play Tic-Tac-Toe!")

#Utility function
# exits if 'quit' is entered
# saves input to file
logfile = 'tttlog.txt'
def utility(Input):
        if Input.upper() == 'QUIT': # quit if quit is entered
            with open(logfile, 'a') as save_actions: # a = append ##next line = pretty as new line in file
                save_actions.write(f'User input quit request: {Input}\n')  #\n for new line
            sys.exit()
        # logging # optional
        with open(logfile, 'a') as save_actions: # a = append ##next line = pretty as new line in file
            save_actions.write(f'User Input: {Input}\n') # Quotes don't work, must be ' #\n for new line


# player name function #comment properly
def get_player_name(NameAsk="Enter your name:"):
   while True:
      try:
      # request player name, pass through utility function
        PlayerName = input(NameAsk)
        utility(PlayerName) # pass input through utility function to log or quit
        if not PlayerName.isalpha():
            raise ValueError
        return PlayerName
      except ValueError:
            print(f"Please try again-{PlayerName} is not valid. Provide a name, or 'quit' to exit")



# select marker function / player
def select_marker(Player):
   while True:
      try:
         print(f"{Player}, would you like to play as X or O (X goes first)")
         MarkerRaw = input("X or O?") #force to upper #change to player x or depending on choice
         utility(MarkerRaw) # pass input through utility function to log or quit
         Marker= MarkerRaw.upper()
         if(Marker == 'X' or Marker == 'O'):
            print(f"{Player} selected: {Marker}")
            return Marker
         else:
            assert(False) # force assertion so further errors can be managed
      except AssertionError: #assertionerror part of py
         print("Please enter x, o, or quit to exit")

#versus function
def select_versus(Player, PlayerMarker):
#   if Player1Marker == "X"
    print(f"versus function:{Player} is playing {PlayerMarker}")
    if PlayerMarker == "X":
        Player2Marker = "O"
    elif PlayerMarker =="O":
        Player2Marker = "X"
    print(f"versus function: Opponent is playing {Player2Marker}")
    return Player2Marker

###BOARD FUNCTIONS

## function to display board ###
def TTTBoard_Display():
    print("TicTacToe Board")
    print("+-----------+")
    print(f"| {TTTBoard['A']} | {TTTBoard['B']} | {TTTBoard['C']} |")
    print("-------------")    
    print(f"| {TTTBoard['D']} | {TTTBoard['E']} | {TTTBoard['F']} |") 
    print("-------------")
    print(f"| {TTTBoard['G']} | {TTTBoard['H']} | {TTTBoard['I']} |") 
    print("+-----------+")


#player move
def TTT_Move(CurrentPlayer,PlayerMarker):
    while True:
        PlaceMark = input(f"Player {CurrentPlayer}, enter A-I to place your {PlayerMarker} ").upper()
        utility(PlaceMark)
        if PlaceMark in TTTBoard:
            TTTBoard[PlaceMark] = PlayerMarker
            TTTBoard_Display()
            break
        else:
            print(f"Select a letter A-I to place your {PlayerMarker}, or quit to exit.")

# win conditions function # fix player
def CheckForWin(Player):
    WinConditions = [
        ["A","B","C"],["D","E","F"],["G","H","I"],# Horizontal
        ["A","D","G"],["B","E","H"],["C","F","I"],# Vertical
        ["A","E","I"],["G","E","C"] # Diagonal
    ]
    for Conditions in WinConditions:
        if TTTBoard[Conditions[0]] == TTTBoard[Conditions[1]] == TTTBoard[Conditions[2]] == Player:
            return True
    return False

### MAIN FUNCTION
def main():
    salutation()
    #get player 1 name
    Player1 = get_player_name()
    print(f"Hello {Player1}")
    Player1Marker = select_marker(Player1)
    print(f"{Player1} is playing {Player1Marker}")
    #Player2Select
    Player2Marker= select_versus(Player1,Player1Marker)
    Player2 = "Placeholder PC" #placeholder?
    print(f"{Player2} is playing {Player2Marker}")
    #CurrentPlayer="X"
    TTTBoard_Display()#.center(Centerwidth)
    #TTT_Move()
    if Player1Marker == "X":
        TTT_Move(Player1,Player1Marker)


    #CurrentPlayer=first_move()
# call main

main()
