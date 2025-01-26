##README.md

Ok - went through again and cleaned it up a bit. Submission is asking for this in a .py file.
Do we want to set up a shared workspace / repo?
 
Note - we don't need to stick to a method like move selection if there's a better one, so having the move slots be 1-9 is an option, and may look better on display.
 
I'm not going to tag everything, but planning-wise, I'm mentally putting this into 3 categories:
[GO] Things we can do now
[?] Gaps - things we know we need, but don't know how to accomplish yet.
[EC] Extra Credit - we get bonus points if we manage to do this, but it's not required.
 
#Team Sea
#Tic-Tac-Toe
 
# Submission 1
Submission1: Pseudo-code of overall structures, Choosing a player, displaying a board and input validation methods. Define your next steps.
 
 
### Structure & Needed items
# read / write to external file
# commenting on all final code

### On startup:
# Salutation ("Hi! Do you want to play a game? Etc)
 
initial inputs
Ask for player name
Ask for player x o selection
who plays first? -x always
[EC] 2 player or 1 player
Playing against the computer is a requirement, 2 player option is not.
 
Logic
Take player inputs and return greeting, asking the next question (x o selection) using the players' name.
Write this to a save file named tictactoe.txt
Display the Game Board (Unplayed - no empty slots)
 
Game Board
Grid assignment 1-3 vertical columns, a-c horizontal rows
<define unplayed grid> / example
There should be no blank or empty cells. If a cell has not been moved on, it should display either a placeholder or it's value (A1, A2, A3)
board grid filled out (example for reference)
 
Playing inputs
player move selection
Player should enter A1 to place their marker in the top left corner of the grid
C3 would place their marker in the bottom right
 
Logic
[?] Write each move to a save file named tictactoe.txt
Computer move selection (random or algo based)
[EC] bonus points if computer moves are algorithm based instead of random
Turn logic - After one player makes a move, progress to other player.
Display the updated board after every turn
Reject invalid input gracefully (program should not break, and ask for correct input instead)
Detection of 3 in a row
Diagonal
Vertical
Horizontal
Conditions so that a move cannot be overwritten by either player (if one person selects A1, the computer or another player should not be able to select A1)
Responses / text to accompany moves (It's <player>'s turn now…) etc
[EC] I don't see a request for logging, but optionally, writing every input and event to a tictactoemonitor.txt file. (this is something that is useful to know how to do in general)
 
Win conditions [exit strategy]
When a player gets 3 in a row, (vertically, horizontally, diagonally) they win.
Print a victory message for that player and exit
If there is no way for either player to win (no more moves available and not meeting win condition)
Print a stalemate message and exit


-celia  she/her
