#tictactoe personal main
### Team Sea ###
#     (..)     #
#   (((())))   #
################
# Celia Chesebro 
# Ian Hutcheson
# Nathaniel Mcrae

### TO DO
# def name style consistent - all camel or lower
# minimax algo
# fix centering?
# add explanation for quit

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

### COMPLETED Other ###
# stalemate logic
# no recursive loops - turn into while

### IMPORTS
import random # used in greeting, first move if computer
import sys # used to exit when quit is given as input

#### Board Dictionary
TTTBoard = {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I"}
##separate tuple of places for use in other logic 
# (dictionary can't be called positionally for random, compare list for stalemate logic)
PlaceList = ("A", "B", "C", "D", "E", "F", "G", "H", "I")

# save file
savefile = 'tictactoe.txt'


###### Functions
# salutation
#needs import random - small test of rand concept.
def Salutation():
   print(OpCreditText.center(Centerwidth))
   print("")
   Greeting = ["Hey", "Hi", "Hello"]
   Salutation = Greeting[random.randint(0, len(Greeting) - 1)]
   print(f"{Salutation} there! Let's play Tic-Tac-Toe!")
   print("You can enter 'quit' at any point to exit the program.")

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
         print(f"{Player}, would you like to play as X or O? (X goes first)")
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
# returns Player2Marker
#args, Player, PlayerMarker
# these are called by Player 1s name and marker, 
# but not naming the same to keep variables separate
def assign_VersusMarker(Player,PlayerMarker):
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
         print("Selected: Computer")
         Player2 = "OctoBot"
         #write selection to save file
         with open(savefile, 'a') as save_input: # a = append 
            save_input.write(f'Player Two will be played by the OctoBot\n') #\n for new line
         return Player2
    # if another player is selected, call the get_PlayerName() function, with different text prompt
    elif PlayerTwoSelect == 'B':
         print("Selected: Player")
         Player2 = get_PlayerName("Enter your name, Player Two:")
         #write selection to save file
         with open(savefile, 'a') as save_input: # a = append 
            save_input.write(f'Player Two will be played by {Player2}\n') #\n for new line
         return Player2
    else:
        print("Please enter A, B, or quit to exit")
        get_PlayerTwo()


###BOARD FUNCTIONS

## function to display TicTacToe board ###
def display_TTTBoard():
    #board config
    TTTBoardVar=f"""
    +-----------+
    | {TTTBoard['A']} | {TTTBoard['B']} | {TTTBoard['C']} |
    -------------   
    | {TTTBoard['D']} | {TTTBoard['E']} | {TTTBoard['F']} |
    -------------
    | {TTTBoard['G']} | {TTTBoard['H']} | {TTTBoard['I']} |
    +-----------+"""
    # print board
    print(TTTBoardVar) #.center(Centerwidth)) 

## win conditions function ###
# returns false until a given marker is present in all three slots of one of the conditions
def CheckForWin(PlayerMarker):
    #list of lists of possible win conditions
    WinConditions = [
        # Horizontal
        ["A","B","C"],
        ["D","E","F"],
        ["G","H","I"],
        # Vertical
        ["A","D","G"],
        ["B","E","H"],
        ["C","F","I"],
        # Diagonal
        ["A","E","I"],
        ["G","E","C"] 
                     ]
    # for each list in the list of win conditions
    for Conditions in WinConditions:
        # if all 3 values in any list match a player marker, then it is 3 in a row , return true
        if TTTBoard[Conditions[0]] == TTTBoard[Conditions[1]] == TTTBoard[Conditions[2]] == PlayerMarker:
            return True
    return False


## stalemate conditions function
# checks if any moves are left and
# displays message, exits if there are none
def CheckForStalemate():
   TTTValues = list(TTTBoard.values())
   # isdisjoint() checks if the list of values currently in the Tic Tac Toe Board
   # have any elements in common with the tuple of available places
   # if there are none, there are no moves left, and it is a stalemate
   if set(PlaceList).isdisjoint(TTTValues):
      # tell the player there are no more moves
      print(StalemateOctopus.center(Centerwidth))
      # update the save file with exit reason
      with open(savefile, 'a') as save_input: # a = append 
         save_input.write(f'Stalemate: No moves left, exiting. \n') #\n for new line
      sys.exit()
   else:
      #status print - uncomment to observe progress
      #print("at least one move left")
      pass


### TEXT ### ###TEXT #### 
Centerwidth = 80 
#opening credits
OpCreditText= f"""
### TEAM SEA ###
#     (..)     #
#   (((())))   #
####PRESENTS####
##TIC#TAC#TOE###
"""
#victory 
VictoryOctopus=f"""
#Congratulations!#
#    ( (..) )    #
#     ((()))     #
##################
"""

#stalemate
StalemateOctopus=f"""
# No More Moves! #
#    (((())))    #
#      (xx)      #
##################
"""

### Move Logic
# player move function
def TTT_Move(CurrentPlayer,PlayerMarker):
    while True:
        PlaceMark = input(f"Player {CurrentPlayer}, enter A-I to place your {PlayerMarker} ").upper()
        exit_utility(PlaceMark) # pass input through the utility function that checks for 'quit' 
        # if input is in the list of moves
        if PlaceMark in TTTBoard:
            print(TTTBoard[PlaceMark])
            # check if the location is already taken.
            if TTTBoard[PlaceMark] not in ["X","O"]:
               TTTBoard[PlaceMark] = PlayerMarker
               # update save file with this info
               with open(savefile, 'a') as save_input: # a = append 
                  save_input.write(f'Player {CurrentPlayer} put their {PlayerMarker} on {PlaceMark} successfully. \n') #\n for new line
               #display the board
               display_TTTBoard()
               break
            else:
               # if place is taken, display message and ask player to try again.
               print(f"Oops! {PlaceMark} is taken by an {TTTBoard[PlaceMark]}. try again!")
               # update save file with this info
               with open(savefile, 'a') as save_input: # a = append 
                  save_input.write(f'Player {CurrentPlayer} tried to put their {PlayerMarker} on {PlaceMark}, but it was taken by an {TTTBoard[PlaceMark]}. \n') #\n for new line
        else:
            print(f"Select a letter A-I to place your {PlayerMarker}, or quit to exit.")

#function to have computer randomly select move ###
def Octo_Move(CurrentPlayer,PlayerMarker):
        # randomly choose a place from list of places
        PlacePick = random.randint(0, len(TTTBoard) - 1)
        # using list of places as dictionary used for the board is not positional.
        print(f"{CurrentPlayer} is playing {PlaceList[PlacePick]}")
        #check if location is taken, if not place Octo Marker
        if TTTBoard[PlaceList[PlacePick]] not in ["X","O"]:
            TTTBoard[PlaceList[PlacePick]] = PlayerMarker
            # update save file with this info
            with open(savefile, 'a') as save_input: # a = append 
               save_input.write(f'The OctoBot put their {PlayerMarker} on {PlacePick} successfully. \n') #\n for new line
            #display the board
            display_TTTBoard()
        else:
            # if move was taken, put in the save file, try again
            print(f"{PlaceList[PlacePick]} taken...")
            # update save file with this info
            with open(savefile, 'a') as save_input: # a = append 
               save_input.write(f'The OctoBot put their {PlayerMarker} on {PlacePick} but it was taken. \n') #\n for new line
            #call move function to try again   
            Octo_Move(CurrentPlayer,PlayerMarker)


### Supporting Gameplay functions

#Function to switch between players
#using index properties of lists
#args: Current player, list of players
def TurnLogic(CurrentPlayer, Players):
    #current player index from list of players
   current_player_index = Players.index(CurrentPlayer)
    #next player is current player index + 1 mod length of list 
    # (with two players this just switches between the two) 
   next_player_index = (current_player_index + 1) % len(Players)
   #update save file with switch
   with open(savefile, 'a') as save_input: # a = append 
      save_input.write(f'TurnLogic: Switching from player {Players[current_player_index]} to player {Players[next_player_index]}. \n') #\n for new line
   # return the next player in the list as the current player
   return Players[next_player_index]


# logic for first move, so that x always goes first
# returns next CurrentPlayer 
def first_TTT_Play():
    # initialize CurrentPlayer variable here or quitting leads to "not defined" errors
    # in next play
    CurrentPlayer = ["PlayerPlaceholder","MarkerPlaceholder"]
    # if player 1 is x, they go first
    if Player1Marker == "X":
        TTT_Move(Player1,Player1Marker)
        CurrentPlayer = [Player1,Player1Marker]
        #pass player 1 to the turn logic to return the next player
        CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)
        return CurrentPlayer
    # if player 1 is not x, player 2 goes first
    else:
        # if current player is the computer, call the Octo_Move() function
        if Player2 == "OctoBot":
            Octo_Move(Player2,Player2Marker)
            CurrentPlayer = [Player2,Player2Marker]
            #pass player thru the turn logic to return the next player
            CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)
            return CurrentPlayer
        # if current player is a human, let them choos their move.
        else:
            TTT_Move(Player2,Player2Marker)
            CurrentPlayer = [Player2,Player2Marker]
            #pass player thru the turn logic to return the next player
            CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)
            return CurrentPlayer
      

### MAIN LOGIC ## 
# Main TicTacToe Loop
def TTT_Main():
   #pass currentplayer into function
   #arguments called positionally here - name[0],marker[1]
   global CurrentPlayer
   # while no player markers meet the win condition
   # Check for win is called twice - once here to enable a while loop, 
   # and again inline to actually check for win at the right time and return victory message
   while CheckForWin(CurrentPlayer[1]) is False:
      # if current player is the computer, call Octo_Move
      if CurrentPlayer[0] == "OctoBot":
            Octo_Move(CurrentPlayer[0],CurrentPlayer[1])
      #otherwise, ask CurrentPlayer for their choice
      else:
            TTT_Move(CurrentPlayer[0],CurrentPlayer[1])
      # Check for win, display message if true and exit
      if CheckForWin(CurrentPlayer[1]) is True:
         print(f"Player {CurrentPlayer[0]} won!")
         print(VictoryOctopus.center(Centerwidth))
         # update the save file with this info
         with open(savefile, 'a') as save_input: # a = append 
            save_input.write(f'"Player {CurrentPlayer[0]} won. Exiting.") \n') #\n for new line
         sys.exit()
      else:
         pass
      #check for stalemate
      CheckForStalemate()
      #switch players
      CurrentPlayer = TurnLogic(CurrentPlayer,PlayerList)

      #then repeate loop
      #TTT_Main() # naughty, using CheckForWin at top of while loop avoids this.
  
### CALLS BEGIN ###
#call salutation
Salutation()
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
display_TTTBoard()

#status print
print(f"{Player1} vs {Player2}")#.center(Centerwidth))
print(f"Players gathered, lets play!")

# first move based on who is playing x also returns current player
CurrentPlayer= first_TTT_Play()
#status print - may be decommented to observe logic progress
#print(f"First Move complete: Current Player is {CurrentPlayer[0]}")

#begin main loop used for rest of game
TTT_Main()

#fin
