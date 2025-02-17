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

#fix print opening credits centered.
Centerwidth = 60 
OpCreditText= """
### TEAM SEA ###
#     (..)     #
#   (((())))   #
####PRESENTS####
##TIC#TAC#TOE###
"""

###### WORKING LINE
# salutation
#needs import random
def salutation():
   Greeting = ["Hey", "Hi", "Hello"]
   Salutation = Greeting[random.randint(0, len(Greeting) - 1)]
   print(Salutation, "there! Let's play Tic-Tac-Toe!")

#Utility function
# exits if 'quit' is entered
# saves input passed through it to file
savefile = 'tictactoe.txt'
def utility(Input):
        if Input.upper() == 'QUIT': # quit if quit is entered
            with open(savefile, 'a') as save_actions: # a = append ##next line = pretty as new line in file
                save_actions.write(f'User input quit request: {Input}\n')  #\n for new line
            sys.exit()
        # logging # optional
        with open(savefile, 'a') as save_actions: # a = append ##next line = pretty as new line in file
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
# player 1s input
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

## win conditions function ###
# returns false until a given marker is present in all three slots of one of the conditions
def CheckForWin(PlayerMarker):
    WinConditions = [
        ["A","B","C"],["D","E","F"],["G","H","I"],# Horizontal
        ["A","D","G"],["B","E","H"],["C","F","I"],# Vertical
        ["A","E","I"],["G","E","C"] # Diagonal
    ]
    for Conditions in WinConditions:
        if TTTBoard[Conditions[0]] == TTTBoard[Conditions[1]] == TTTBoard[Conditions[2]] == PlayerMarker:
            return True
    return False

### Move Logic
# player move function
def TTT_Move(CurrentPlayer,PlayerMarker):
    while True:
        PlaceMark = input(f"Player {CurrentPlayer}, enter A-I to place your {PlayerMarker} ").upper()
        utility(PlaceMark) # pass input through the utility function that logs the input and checks for 'quit' 
        # if input is in the list of moves
        if PlaceMark in TTTBoard:
            print(TTTBoard[PlaceMark])
            # check if the location is already taken.
            if TTTBoard[PlaceMark] not in ["X","O"]:
                TTTBoard[PlaceMark] = PlayerMarker
                TTTBoard_Display()
                break
            else:
                print(f"Oops! {PlaceMark} is taken by an {TTTBoard[PlaceMark]}. try again!")
        else:
            print(f"Select a letter A-I to place your {PlayerMarker}, or quit to exit.")

#function to have computer randomly select move ###
def Octo_Move(CurrentPlayer,PlayerMarker):
        PlacePick = random.randint(0, len(TTTBoard) - 1)
        # using list of places as dictionary used for the board is not positional.
        Places = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        print(f"{CurrentPlayer} is playing {Places[PlacePick]}")
        #check if location is taken
        if TTTBoard[Places[PlacePick]] not in ["X","O"]:
            TTTBoard[Places[PlacePick]] = PlayerMarker
            TTTBoard_Display()
        else:
            print(f"{Places[PlacePick]} is taken, trying again.")


#Function to switch between players
#using index properties of lists
def switch_player(CurrentPlayer, Players):
    #print("switching...", CurrentPlayer)
    current_index = Players.index(CurrentPlayer)
    #print("current_index.", current_index)
    next_index = (current_index + 1) % len(Players)
    #print("next_index.", next_index)
    #print("switching to:", Players[next_index])
    return Players[next_index]


# logic for first move, so that x always goes first
def first_move():
    global Player1Marker
    if Player1Marker == "X":
        TTT_Move(Player1,Player1Marker)
        CurrentPlayer = [Player1,Player1Marker]
        print("first move completed, current player:", CurrentPlayer)
        CurrentPlayer = switch_player(CurrentPlayer,PlayerList)
        return CurrentPlayer
    else:
        Octo_Move(Player2,Player2Marker)
        CurrentPlayer = [Player2,Player2Marker]
        print("first move completed, current player:", CurrentPlayer)
        CurrentPlayer = switch_player(CurrentPlayer,PlayerList)
        return CurrentPlayer
    
      

### MAIN LOGIC ## 
# Main TicTacToe Loop
def TTT_Main():
    global CurrentPlayer
    while CheckForWin(CurrentPlayer[1]) is False:
        if CurrentPlayer[0] == "Placeholder PC":
            Octo_Move(CurrentPlayer[0],CurrentPlayer[1])
        else:
            TTT_Move(CurrentPlayer[0],CurrentPlayer[1])
        if CheckForWin(CurrentPlayer[1]) is True:
            print(f"Player {CurrentPlayer[0]} won!")
            sys.exit()
        else:
            pass
        CurrentPlayer = switch_player(CurrentPlayer,PlayerList)
        print("switching to: ",CurrentPlayer[0])
        TTT_Main()
    else:
        print(f"Player {CurrentPlayer[0]} won!")
        sys.exit()

# while no one has one
#    while CheckForWin(TestPlayerMarker) is False:

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
print(f"{Player2} is playing {Player2Marker}")

#Define player list used for switching
PlayerList = [[Player1, Player1Marker], [Player2 , Player2Marker]]

# display the board
TTTBoard_Display()


#status print - may be decommented to observe logic progress
print(f"Players gathered, starting first move")


CurrentPlayer= first_move()
#status print - may be decommented to observe logic progress
print(f"First Move complete: Current Player is {CurrentPlayer[0]}")
TTT_Main()
