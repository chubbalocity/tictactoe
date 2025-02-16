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

#versus function, Designates marker of opponent based on
def select_versus(Player, PlayerMarker):
#   if Player1Marker == "X"
    print(f"versus function:{Player} is playing {PlayerMarker}")
    if PlayerMarker == "X":
        Player2Marker = "O"
    else:
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

# win conditions function # fix
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

## Move Logic
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

#function to have computer randomly select move
def Octo_Move(CurrentPlayer,PlayerMarker):
        PlacePick = random.randint(0, len(TTTBoard) - 1)
        Places = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        #Places = [TTTBoard]
        print(f"{CurrentPlayer} is playing {Places[PlacePick]}")
        if Places[PlacePick] in TTTBoard:
            TTTBoard[Places[PlacePick]] = PlayerMarker
            TTTBoard_Display()



# versus_PCorNPC
#def versus_PCorNPC()
#print(f"Will {OtherMarker} be played by another player or the computer")
#SelectPlayer = input("1 for a player, 2 to play the computer:")


# turn logic
# def first_move(Player1Marker):
#     if Player1Marker == "X":
#         TTT_Move(Player1,Player1Marker)
#     else:
#         Octo_Move(Player2,Player2Marker)



def first_move():
    if Player1Marker == "X":
        TTT_Move(Player1,Player1Marker)
        CurrentPlayer = Player1#,Player1Marker
        NextPlayer = Player2#,Player2Marker
        return CurrentPlayer,NextPlayer
    else:
        Octo_Move(Player2,Player2Marker)
        CurrentPlayer = Player2#,Player2Marker
        NextPlayer == Player1#,Player1Marker
        return CurrentPlayer,NextPlayer

def play_TTT():
    #while CheckForWin() is False:
    print(CheckForWin)
    for player in Players:
       if player == Player2:
        Octo_Move(Player2,Player2Marker)
    else:
        TTT_Move(Player1,Player1Marker)
    

### MAIN LOGIC ## 
#call greeting
salutation()
#get player 1 name
Player1 = get_player_name()
print(f"Hello {Player1}")
Player1Marker = select_marker(Player1)
print(f"{Player1} is playing {Player1Marker}")
#Set Player 2 to computer
Player2Marker= select_versus(Player1,Player1Marker)
Player2 = "Placeholder PC" #placeholder?
Players = [Player1,Player2]

print(f"{Player2} is playing {Player2Marker}")
TTTBoard_Display()
  #TTT_Move()
    #first_move()


first_move()
#print(f"Current Player is {CurrentPlayer}")
play_TTT()



    #CurrentPlayer=first_move()
# call main
#def main():
#main()
