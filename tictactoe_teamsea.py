#tictactoe team sea
### Team Sea ###
#     (..)     #
#   (((())))   #
################
# Celia Chesebro 
# Ian Hutcheson
# Nathaniel Mcrae


### TO DO NOTES
# Review comments to combine separate programs

### Program Begin
## IMPORTS
import random # used in greeting, first move if computer
import sys # used to exit when quit is given as input
import time #import time

# save file
savefile = 'tictactoe.txt'
#set filename for logging
filename = 'tttlog.txt' # optional

#### Board Dictionary
#define values to display in middle of each graphic square
squares = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}    




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
