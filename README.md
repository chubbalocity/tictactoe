### Team Sea ###
#     (..)     #
#   (((())))   #
################
# Celia Chesebro 
# Ian Hutcheson
# Nathaniel Mcrae


### Tic-Tac-Toe ###
 
# Submission 1
#Submission1: Pseudo-code of overall structures, Choosing a player, displaying a board and input validation methods. Define your next steps.

##Next Steps.
# Establish repo and working spaces
# Begin work on game file with
# initial inputs and input validations
# finalize game board 
# begin defining functions
 
### Structure & Needed items
## General todos
# read / write to external file
# commenting on all final code

####### tic tac toe pseudo code / structure
### On startup:
# Salutation ("Hi! Do you want to play a game? Etc)
 
#initial inputs
#Ask for player name
#Ask for player x o selection
#    who plays first? -x always

#[EC] 2 player or 1 player
#    Playing against the computer is a requirement, 2 player option is not.

 
### starting Logic
#Take player inputs and return greeting, asking the next question (x o selection) using the players' name.
#Write this to a save file named tictactoe.txt
#Display the Game Board (Unplayed - no empty slots)
# type 'quit' at any time to quit program
 
#Game Board
#Grid assignment 1-3 vertical columns, a-c horizontal rows

#    -------------
#    | A | B | C |
#    -------------
#    | D | E | F |
#    -------------
#    | G | H | I |
#    -------------

#   There should be no blank or empty cells. If a cell has not been moved on, 
# it should display either a placeholder or it's value (A, B, C)

# board grid partially filled out (example for reference)
#    -------------
#    | O | X | C |
#    -------------
#    | X | O | X |
#    -------------
#    | O | O | X |
#    -------------
 
#Playing inputs
#player move selection

#    Player should enter A1 to place their marker in the top left corner of the grid
#    C3 would place their marker in the bottom right

 
### Gameplay Logic
#[?] Write each move to a save file named tictactoe.txt
#Computer move selection (random or algo based)

#    [EC] bonus points if computer moves are algorithm based instead of random

#Turn logic - After one player makes a move, progress to other player.
#Display the updated board after every turn
#Reject invalid input gracefully (program should not break, and ask for correct input instead)
#Detection of 3 in a row
#    Diagonal
#    Vertical
#    Horizontal
# inlude ability to type 'quit' at any time to quit program
#Conditions so that a move cannot be overwritten by either player (if one person selects A1, the computer or another player should not be able to select A1)
#Responses / text to accompany moves (It's <player>'s turn now…) etc
#[EC] I don't see a request for logging, but optionally, writing every input and event to a tictactoemonitor.txt file. (this is something that is useful to know how to do in general)
 
#Win conditions [exit strategy]
#When a player gets 3 in a row, (vertically, horizontally, diagonally) they win.
#    Print a victory message for that player and exit

#If there is no way for either player to win (no more moves available and not meeting win condition)
#    Print a stalemate message and exit
