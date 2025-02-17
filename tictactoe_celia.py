#tictactoe personal main
### Team Sea ###
#     (..)     #
#   (((())))   #
################
# Celia Chesebro 
# Ian Hutcheson
# Nathaniel Mcrae

### TO DO
# def name style consistent
# minimax algo
# fix centering?
# freview logging to tictactoe.txt

### COMPLETED REQUIREMENTS
# ask user for name
# ask user by name if they want to play x or o (x goes first)
# automatically assigns other marker to the other player.
# give option to play pc or player
# computer selects position (randomly)
# display the board after each run
# handle incorrect inputs
# add move logging to tictactoe.txt
# prints message for winner and exits

### COMPLETED EXTRAS ###
# stalemate logic


### IMPORTS
import random # used in greeting, first move if computer
import sys # used to exit when quit is given as input

#### Board Dictionary
TTTBoard = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I"}
##separate tuple of places for use in other logic
PlaceList = ("A", "B", "C", "D", "E", "F", "G", "H", "I")

# save file
savefile = 'tictactoe.txt'
#### OPTIONAL LOGGING
 #log file
logfile = 'tttlog.txt'   
# logging # optional
#with open(logfile, 'a') as logging_opt: # a = append ##next line = pretty as new line in file
#     logging_opt.write(f'{Takeinput}\n') # Quotes don't work, must be ' #\n for new line
#     logging_opt.write(f'Dummy test log line. \n') # test logging 1
#     logging_opt.write(f'fake programattic thing that happens because of "{Takeinput}". \n') # test logging 2



###### WORKING LINE
# salutation
#needs import random - small test of rand concept.
def salutation():
   Greeting = ["Hey", "Hi", "Hello"]
   Salutation = Greeting[random.randint(0, len(Greeting) - 1)]
   print(Salutation, "there! Let's play Tic-Tac-Toe!")

#Utility function
# exits if 'quit' is entered
def exit_utility(Input):
        if Input.upper() == 'QUIT': # quit if quit is entered
            with open(savefile, 'a') as save_input: # a = append ##next line = pretty as new line in file
                save_input.write(f'User input quit request: {Input}\n')  #\n for new line
            sys.exit()
        else:
            pass


# function to get a players name
def get_PlayerName(NameAsk="Enter your name:"):
   while True:
      try:
      # request player name
         PlayerName = input(NameAsk)
         exit_utility(PlayerName) # pass input through utility function if user wants to quit
         if not PlayerName.isalpha():
            raise ValueError
         #write selection to save file
         with open(savefile, 'a') as save_input: # a = append ##next line = pretty as new line in file
            save_input.write(f'User input {PlayerName} for PlayerName.\n')  #\n for new line
         return PlayerName
      except ValueError:
            print(f"Please try again-{PlayerName} is not valid. Provide a name, or 'quit' to exit")
            #write rejected input to save file
            with open(savefile, 'a') as save_input: # a = append ##next line = pretty as new line in file
                save_input.write(f'User input {PlayerName} was not valid, retrying.\n')  #\n for new line


# function for player one to select their marker
def select_Player1Marker(Player):
   while True:
      try:
         # ask player for x or o, tell them x goes first.
         print(f"{Player}, would you like to play as X or O (X goes first)")
         Marker = input("X or O?").upper() #change to uppercase
         exit_utility(Marker) # pass input through utility function if user wants to quit
         if(Marker == 'X' or Marker == 'O'):
            print(f"{Player} selected: {Marker}")
            #write selection to save file
            with open(savefile, 'a') as save_input: # a = append 
               save_input.write(f'{Player} chose the Marker {Marker} \n') #\n for new line
            return Marker
         else:
            assert(False) # force assertion so further errors can be managed
      except AssertionError: #assertionerror part of py
         print("Please enter x, o, or quit to exit")

#versus function, Designates marker of opponent based on
# player 1s input. (assignes O if player chooses X and vice versa)
def assign_VersusMarker(Player, PlayerMarker):
      if PlayerMarker == "X":
         Player2Marker = "O"
      else:
         Player2Marker = "X"
      # update file with status
      with open(savefile, 'a') as save_input: # a = append 
         save_input.write(f'Player Two is assigned the Marker {Player2Marker} \n') #\n for new line
      return Player2Marker

#function to ask if player two is pc or person
# give option of a computer or b person
def get_PlayerTwo():
    print("Would you like to play the computer or another player?")
    PlayerTwoSelect= input("A for computer, B for a player:").upper()
    exit_utility(PlayerTwoSelect) # pass input through utility function if user wants to quit
    # OctoBot is the static method for the game to know if the computer is playing.
    if PlayerTwoSelect == 'A':
         print("selected: computer")
         Player2 = "OctoBot"
         #write selection to save file
         with open(savefile, 'a') as save_input: # a = append 
            save_input.write(f'Player Two will be played by the OctoBot\n') #\n for new line
         return Player2
    # if another player is selected, call the get_PlayerName() function, with different text prompt
    elif PlayerTwoSelect == 'B':
         print("selected: player")
         Player2 = get_PlayerName("Enter your name, Player Two:")
         #write selection to save file
         with open(savefile, 'a') as save_input: # a = append 
            save_input.write(f'Player Two will be played by {Player2}\n') #\n for new line
         return Player2
    else:
        print("Please enter A, B, or quit to exit")
        get_PlayerTwo()


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


## stalemate conditions function
# checks if any moves are left and
# displays message, exits if there are none
def CheckForStalemate():
   TTTValues = list(TTTBoard.values())
   if set(PlaceList).isdisjoint(TTTValues):
      print(StalemateOctopus)
      with open(savefile, 'a') as save_input: # a = append 
         save_input.write(f'Stalemate: No moves left, exiting. \n') #\n for new line
      sys.exit()
   else:
      #status print - uncomment to observe progress
      #print("at least one move left")
      pass


### TEXT ### ###TEXT #### 
Centerwidth = 60 
#opening credits
OpCreditText= """
### TEAM SEA ###
#     (..)     #
#   (((())))   #
####PRESENTS####
##TIC#TAC#TOE###
"""
#victory 
VictoryOctopus='''
#    ( (..) )    #
#     ((()))     #'''

#stalemate
StalemateOctopus='''
# No More Moves! #
#    (((())))    #
#      (xx)      #
'''

### Move Logic
# player move function
def TTT_Move(CurrentPlayer,PlayerMarker):
    while True:
        PlaceMark = input(f"Player {CurrentPlayer}, enter A-I to place your {PlayerMarker} ").upper()
        exit_utility(PlaceMark) # pass input through the utility function that logs the input and checks for 'quit' 
        # if input is in the list of moves
        if PlaceMark in TTTBoard:
            print(TTTBoard[PlaceMark])
            # check if the location is already taken.
            if TTTBoard[PlaceMark] not in ["X","O"]:
               TTTBoard[PlaceMark] = PlayerMarker
               with open(savefile, 'a') as save_input: # a = append 
                  save_input.write(f'Player {CurrentPlayer} put their {PlayerMarker} on {PlaceMark} successfully. \n') #\n for new line
               TTTBoard_Display()
               break
            else:
               print(f"Oops! {PlaceMark} is taken by an {TTTBoard[PlaceMark]}. try again!")
               with open(savefile, 'a') as save_input: # a = append 
                  save_input.write(f'Player {CurrentPlayer} tried to put their {PlayerMarker} on {PlaceMark}, but it was taken by an {TTTBoard[PlaceMark]}. \n') #\n for new line
        else:
            print(f"Select a letter A-I to place your {PlayerMarker}, or quit to exit.")

#function to have computer randomly select move ###
def Octo_Move(CurrentPlayer,PlayerMarker):
        PlacePick = random.randint(0, len(TTTBoard) - 1)
        # using list of places as dictionary used for the board is not positional.
        print(f"{CurrentPlayer} is playing {PlaceList[PlacePick]}")
        #check if location is taken
        if TTTBoard[PlaceList[PlacePick]] not in ["X","O"]:
            TTTBoard[PlaceList[PlacePick]] = PlayerMarker
            with open(savefile, 'a') as save_input: # a = append 
               save_input.write(f'The OctoBot put their {PlayerMarker} on {PlacePick} successfully. \n') #\n for new line
            TTTBoard_Display()
        else:
            print(f"{PlaceList[PlacePick]} is taken, trying again.")
            with open(savefile, 'a') as save_input: # a = append 
               save_input.write(f'The OctoBot put their {PlayerMarker} on {PlacePick} but it was taken. \n') #\n for new line
            Octo_Move(CurrentPlayer,PlayerMarker)


### Supporting Gameplay functions

#Function to switch between players
#using index properties of lists
#args: Current player, list of players
def TurnLogic(CurrentPlayer, Players):
    #print("switching...", CurrentPlayer)
   current_player_index = Players.index(CurrentPlayer)
    #print("current_index.", current_index)
   next_player_index = (current_player_index + 1) % len(Players)
   #print("next_index.", next_index)
   #print("switching to:", Players[next_index])
   with open(savefile, 'a') as save_input: # a = append 
      save_input.write(f'TurnLogic: Switching from player {Players[current_player_index]} to player {Players[next_player_index]}. \n') #\n for new line
   return Players[next_player_index]


# logic for first move, so that x always goes first
# returns next CurrentPlayer 
def first_TTT_Play():
    global Player1Marker
    if Player1Marker == "X":
        TTT_Move(Player1,Player1Marker)
        CurrentPlayer = [Player1,Player1Marker]
        #print("first move completed, current player:", CurrentPlayer)
        CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)
        return CurrentPlayer
    else:
        # if current player is the computer, call the Octo_Move() function
        if CurrentPlayer[0] == "OctoBot":
            Octo_Move(Player2,Player2Marker)
            CurrentPlayer = [Player2,Player2Marker]
            #print("first move completed, current player:", CurrentPlayer)
            CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)
            return CurrentPlayer
        # if current player is a human, let them choos their move.
        else:
            TTT_Move(Player2,Player2Marker)
            CurrentPlayer = [Player2,Player2Marker]
            #print("first move completed, current player:", CurrentPlayer)
            CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)
            return CurrentPlayer
      

### MAIN LOGIC ## 
# Main TicTacToe Loop
# 
def TTT_Main():
   global CurrentPlayer
   while CheckForWin(CurrentPlayer[1]) is False:
      if CurrentPlayer[0] == "OctoBot":
            Octo_Move(CurrentPlayer[0],CurrentPlayer[1])
      else:
            TTT_Move(CurrentPlayer[0],CurrentPlayer[1])
      if CheckForWin(CurrentPlayer[1]) is True:
         print(f"Player {CurrentPlayer[0]} won!")
         print(VictoryOctopus)
         with open(savefile, 'a') as save_input: # a = append 
            save_input.write(f'f"Player {CurrentPlayer[0]} won. Exiting.") \n') #\n for new line
         sys.exit()
      else:
         pass
      #check for stalemate
      CheckForStalemate()
      #switch players
      CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)

      #then repeate loop
      TTT_Main()
   # else:
   #    print(f"Why is this triggering?")
   #    sys.exit()

### CALLS BEGIN ###
#call salutation
salutation()
#get player 1 name & greet player by name
Player1 = get_PlayerName()
print(f"Hello {Player1}")

# get player 1 marker by calling function to present choice
Player1Marker = select_Player1Marker(Player1)
print(f"{Player1} is playing {Player1Marker}")

# Set player 2's marker based on player 1's selection
Player2Marker= assign_VersusMarker(Player1,Player1Marker)

#Get player two
# this calls function that asks if user wants to play the computer or another user
Player2 = get_PlayerTwo()
print(f"{Player2} is playing {Player2Marker}")

#Define player list used for switching
PlayerList = [[Player1, Player1Marker], [Player2 , Player2Marker]]

# display the board
TTTBoard_Display()

#status print - may be decommented to observe logic progress
print(f"Players gathered, starting first move")

# first move based on who is playing x also returns current player
CurrentPlayer= first_TTT_Play()
#status print - may be decommented to observe logic progress
#print(f"First Move complete: Current Player is {CurrentPlayer[0]}")

#begin main loop used for rest of game
TTT_Main()

#fin
