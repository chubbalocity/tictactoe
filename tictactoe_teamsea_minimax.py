#tictactoe team sea
### Team Sea ###
#     (..)     #
#   (((())))   #
################
# Celia Chesebro 
# Ian Hutcheson
# Nathaniel Mcrae

### IMPORTS
import random # used in greeting, first move if computer
import sys # used to exit when quit is given as input
import datetime #import datetime

#### Starting Dictionary, list, and variables
# Board Dictionary
TTTBoard = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}  
##separate list of places for use in other logic 
# (dictionary can't be called positionally for random, compare list for stalemate logic)
PlaceList = [1, 2, 3, 4, 5, 6, 7, 8, 9] #define list of available moves
# Set Time variables
Now = datetime.datetime.now() # current date & time
NowTime= Now.time() # just the time

### FILES
# save file
savefile = 'tictactoe.txt' # save file
#log file for logging noisier stuff
logfile = 'tttlog.txt' #set filename for logging


###### Functions
# salutation
#needs import random - small test of rand concept.
def Salutation():
    print(OpCreditText.center(Centerwidth))
    print("")
    Greeting = ["Hey", "Hi", "Hello"]
    Salutation = Greeting[random.randint(0, len(Greeting) - 1)]
    print(f"{Salutation} there! Let's play Tic-Tac-Toe!")
    # show current time (from user system)
    # user friendly time format .strftime()
    FriendlyTime = Now.strftime("%H:%M")
    print(f"The time is now: {FriendlyTime}")
    # note session in save & Log Files
    SaveAndLog(f'Team Sea Tic-Tac-Toe Session begun @ {Now}\n')
    print("You can enter 'quit' at any point to exit the program.")

#Utility function
# function to write some basic logic to both files
def SaveAndLog(Message):
    with open(savefile, 'a') as save_input: 
        save_input.write(Message)
    with open(logfile, 'a') as save_input: 
        save_input.write(Message)

#Utility function
# exits if 'quit' is entered
def exit_utility(Input):
        InputString = str(Input)
        if isinstance(Input, str):
            if InputString.upper() == 'QUIT': # quit if quit is entered
                print("Goodbye")
                # Update Save & Log Files with input
                SaveAndLog(f'User input quit request: {Input} @ {Now}\n') 
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
            # Update Save & Log Files with input
            SaveAndLog(f'User input {PlayerName} for PlayerName.\n')  #\n for new line
            return PlayerName
        except ValueError:
            print(f"Please try again-{PlayerName} is not valid. Provide a name, or 'quit' to exit")
            #write rejected input to save & log file
            SaveAndLog(f'User input {PlayerName} was not valid, retrying.\n')


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
            #write selection to save & log file
            SaveAndLog(f'{Player} chose the Marker {Marker} \n')
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
    # update log file with status
    with open(logfile, 'a') as save_input: # a = append
        save_input.write(f'Player Two is assigned the Marker {Player2Marker}, since {Player} chose {PlayerMarker} \n') #\n for new line
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
         #write selection to save & log files
         SaveAndLog(f'Player Two will be played by the OctoBot\n') #\n for new line
         return Player2
    # if another player is selected, call the get_PlayerName() function, with different text prompt
    elif PlayerTwoSelect == 'B':
         print("Selected: Player")
         # write selection only to log file before calling the appropriate function
         with open(logfile, 'a') as save_input: # a = append
            save_input.write(f'get_PlayerTwo logic: PlayerTwoSelect is another player, calling get_PlayerName\n')
         # call player name logic again for player two
         Player2 = get_PlayerName("Enter your name, Player Two:")
         #write selection to save & log
         SaveAndLog(f'Player Two will be played by {Player2}\n') 
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
    | {TTTBoard[1]} | {TTTBoard[2]} | {TTTBoard[3]} |
    -------------   
    | {TTTBoard[4]} | {TTTBoard[5]} | {TTTBoard[6]} |
    -------------
    | {TTTBoard[7]} | {TTTBoard[8]} | {TTTBoard[9]} |
    +-----------+"""
    # print board
    print(TTTBoardVar) #.center(Centerwidth)) 

## win conditions function ###
# returns false until a given marker is present in all three slots of one of the conditions
def CheckForWin(PlayerMarker):
    with open(logfile, 'a') as save_input: # a = append 
        save_input.write(f'CheckForWin invoked - checking for a victory.\n')
    #list of lists of possible win conditions
    WinConditions = [
        # Horizontal
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        # Vertical
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        # Diagonal
        [1, 5, 9],
        [7, 5, 3]
                     ]
    # for each list in the list of win conditions
    for Conditions in WinConditions:
        # if all 3 values in any list match a player marker, then it is 3 in a row , return true
        if TTTBoard[Conditions[0]] == TTTBoard[Conditions[1]] == TTTBoard[Conditions[2]] == PlayerMarker:
            return True
    with open(logfile, 'a') as save_input: # a = append 
        save_input.write(f'CheckForWin: No Winners.\n')
    return False


#function to update PlaceList with available moves
def remove_AvailablePlaces(Move):
    #status print -optional
    #print(f"Move is {Move}.") # move given
    #status print -optional
    #print(f"Index is is {PlaceList[Move]}.") # index of move
    #status print -optional # removal note
    #print(f"removing  {Move} from list of available moves.")
    PlaceList.remove(Move) #remove user's move from list of available moves (-1 as index starts at zero)
    with open(logfile, 'a') as save_input: # a = append to log file
            save_input.write(f'{Move} removed from list of available moves.\n') #\n for new line
            save_input.write(f'Board Dictionary is: {TTTBoard}\n')
            save_input.write(f'List of Places is: {PlaceList}\n')


## stalemate conditions function
# checks if any moves are left and
# displays message, exits if there are none
def CheckForStalemate():
   #TTTValues = list(TTTBoard.values()) # keeping for posterity
   # isdisjoint() checks if the list of values currently in the Tic Tac Toe Board
   # have any elements in common with the list of available places
   # if there are none, there are no moves left, and it is a stalemate
   #print("List of moves", PlaceList) #status print / troubleshooting
   #print("Current board", TTTValues)#status print / troubleshooting
   # but after incorporating Ian's method, we can just check if the list is empty
   if len(PlaceList) == 0:
   #if set(PlaceList).isdisjoint(TTTValues): # keeping as history
      # tell the player there are no more moves
      print(StalemateOctopus.center(Centerwidth))
      # update the save & log files with exit reason
      SaveAndLog(f'Stalemate: No moves left, exiting. \n') #\n for new line
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
        try:
            #ask player for move
            PlaceMarker = input(f"Player {CurrentPlayer}, enter 1-9 to place your {PlayerMarker} ")
            exit_utility(PlaceMarker) # pass input through the utility function that checks for 'quit' 
            PlaceMark = int(PlaceMarker)
            # if input is in the list of moves
            if PlaceMark in TTTBoard:
                print(TTTBoard[PlaceMark])
                # check if the location is already taken.
                if TTTBoard[PlaceMark] not in ["X","O"]:
                    TTTBoard[PlaceMark] = PlayerMarker
                    # remove the move from the list of available places
                    remove_AvailablePlaces(PlaceMark)
                    # update save/log files with this info
                    SaveAndLog(f'Player {CurrentPlayer} put their {PlayerMarker} on {PlaceMark} successfully. \n') #\n for new line
                    #display the board
                    display_TTTBoard()
                    # status / troubleshooting
                    #print("Current list of available moves: ",PlaceList) # mute, for troubleshooting
                    break
                else:
                    # if place is taken, display message and ask player to try again.
                    print(f"Oops! {PlaceMark} is taken by an {TTTBoard[PlaceMark]}. try again!")
                    # update save/log files with this info
                    SaveAndLog(f'Player {CurrentPlayer} tried to put their {PlayerMarker} on {PlaceMark}, but it was taken by an {TTTBoard[PlaceMark]}. \n') #\n for new line
            
        except ValueError:
            print(f"Please try again, {CurrentPlayer}.  1-9 to place your {PlayerMarker} or 'quit' to exit.")
            with open(logfile, 'a') as save_input: # a = append to log file
                save_input.write("ValueError thrown in move logic, retrying\n")

#function to have computer randomly select move ###
def Octo_Move(CurrentPlayer,PlayerMarker):
    if PlaceList: #check if placelist is not empty
        # randomly choose a place from list of places
        PlacePick = random.randint(0, len(TTTBoard) - 1)
        # using list of places as dictionary used for the board is not positional.
        print(f"{CurrentPlayer} is playing {PlaceList[PlacePick]}")
        #check if location is taken, if not place Octo Marker
        if TTTBoard[PlacePick] not in ["X","O"]:
            TTTBoard[PlacePick] = PlayerMarker
            remove_AvailablePlaces(PlacePick)
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
    else:
        print("No moves available.")

#function to have computer move ###
def Octo_Max(CurrentPlayer,PlayerMarker):
    print(f"\nPlease wait while OctoBot ponders the future...") #add wait message to address longer processing time during first move
    blocking_move = find_blocking_move(PlayerMarker) #check if Octobot is in imminent danger of losing to human
    
    if blocking_move is not None and blocking_move in PlaceList: #if a blocking move is necessary...
        PlacePick = blocking_move #select blocking move as Octobot's move
    else:
        _, PlacePick = minimax(TTTBoard, PlaceList[:], PlayerMarker, depth=4) #proceed with normal minimax logic

    if PlacePick is not None and PlacePick in PlaceList: #ensure that PlacePick is not None and that it exists in list of available moves
        print(f"{CurrentPlayer} is playing {PlacePick}") #advise of current player's move
        TTTBoard[PlacePick] = PlayerMarker #place player's marker on board
        remove_AvailablePlaces(PlacePick) #remove player's move selection from list of available moves
        display_TTTBoard() #draw updated gameboard
        SaveAndLog(f'The OctoBot put their {PlayerMarker} on {PlacePick} successfully. \n') #write turn summary to log.
    else:
        if PlacePick is None: #check if minimax returned None for PlacePick, just in case
            print("Minimax returned None, unable to determine move")
            Octo_Move(CurrentPlayer, PlayerMarker) #invoke Octo_Move to have bot make a random selection as a backup option
        else:
            raise ValueError(f"Minimax selected an invalid move - debugging required.") #advise of error, debugging needed


#function for minimax ###

def minimax(board, available_moves, player, depth=4): #define OctoBot minimax logic, including depth to which forward-thinking calculations will be limited
    opponent = "X" if player == "O" else "O" #evaluate whether OctoBot is playing as X or O

    #define logic for move iterative projections
    if CheckForWin(player): #evaluate if player has won
        return 10 - depth, None #if won, award score as numeric incentive
    elif CheckForWin(opponent): #evaluate if opponent has won
        return -10 + depth, None #award negative score as numeric deterrent
    elif len(available_moves) == 0 or depth == 0: #evaluate if no moves are remaining
        return 0, None
    
    best_score = -float('inf') if player == Player2Marker else float('inf') #assign negative/positive infinity as upper and lower boundaries of score spectrum
    best_move = None #define variable for best move, initially set it as None

    for move in available_moves[:]: #interate over a copy to avoid actual mods to PlaceList
        board[move] = player #write move to board
        available_moves.remove(move) #remove most recent move from list of available moves
        
        score, _ = minimax(board, available_moves, opponent, depth - 1) #make recursive OctoMax call

        board[move] = move #revert the move on the gameboard after minimax calcs
        available_moves.append(move) #restore move to list of available moves after minimax calcs
        available_moves.sort() #sort list of available moves

        #choose best move for maximizing or minimizing player
        if player == Player2Marker: #OctoBot maximizing
            if score > best_score:
                best_score, best_move = score, move 
        else: #human minimizing
            if score < best_score: 
                best_score, best_move = score, move

    return best_score, best_move #return result of minimax calcs

def find_blocking_move(player): #define function to check whether human player win is imminent
    opponent = "X" if player == "O" else "O" #evaluate whether OctoBot is playing as X or O

    for move in PlaceList: #loop through available moves in PlaceList
        TTTBoard[move] = opponent #simulate opponent making that move
        if CheckForWin(opponent): #if that move will result in a win
                TTTBoard[move] = move #Select that move for Octobot
                return move #return that move for further use
        TTTBoard[move] = move #select blocking move as OctoBot's move
    
    return None #Blocking move not necessary

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
   with open(logfile, 'a') as save_input: # a = append 
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
        # if current player is the computer, call the minimax() function
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
      # if current player is the computer, call minimax
      if CurrentPlayer[0] == "OctoBot":
            Octo_Max(CurrentPlayer[0],CurrentPlayer[1])
      #otherwise, ask CurrentPlayer for their choice
      else:
            TTT_Move(CurrentPlayer[0],CurrentPlayer[1])
      # Check for win, display message if true and exit
      if CheckForWin(CurrentPlayer[1]) is True:
         print(f"Player {CurrentPlayer[0]} won!")
         print(VictoryOctopus.center(Centerwidth))
         # update the save file with this info
         SaveAndLog(f'"Player {CurrentPlayer[0]} won. Exiting." \n') #\n for new line
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
