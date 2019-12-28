import random
from board import *
from ai import *

'''
Game Class
----------
This class runs the game with the help of the board class
It handles the logic for the options, refreshing the display,
going forward and back through the options, and checking input
'''
class Game():
  # Constructor
  def __init__(self, mode):
    self.mode = mode

  # This is the main loop that runs the game
  def run(self):
    # Initialize needed variables
    winner = -1
    board = Board()
    turn = 0
    # Continue running the game until there is a winner
    if (self.mode == 2): # 2 Players
      while (winner == -1):
        # Show the board and options
        board.showBoard()
        option = self.getOption()
        if (option == 1): # Choose a location
          loc = self.getLocation()
          if (loc == -2): # If quit, do nothing
            pass
          else:
            if (board.board[loc] == -1): # If the spot is empty
              turn += 1
              board.board[loc] = turn % 2
              winner = board.isOver() # Check if the game is over
            else: # If the spot is taken
              print("You can't steal someone's spot")
              input("Press enter to continue: ")
        elif (option == 2):
          # Clear the screen, show the grid, and wait for input to quit
          board.showGrid()
          input("\nPress enter to exit: ")
        else: # Concede
          winner = turn % 2 # Set the other player to the winner
    else:
      random.seed()
      player_turn = random.randint(0, 1)
      while (winner == -1):
        if (turn == player_turn):
          pass
        else:
          pass

    # Display the winner
    board.showBoard()
    if (winner == 1):
      print("Congragulations X!")
    elif (winner == 0):
      print("Congragulations O!")
    else:
      print("Nice battle, no winner.")

  # This returns a option
  def getOption(self):
    # Show the options and initialize needed variables
    self.showOptions()
    user_opt = 0
    allowed_opts = (1, 2, 3)
    # Validate data
    while (not(user_opt in allowed_opts)):
      try:
        user_opt = int(input(""))
        if (not(user_opt in allowed_opts)):
          print("Invalid input\n")
      except ValueError:
        print("Invalid input")
    return user_opt

  # This shows the options
  def showOptions(self):
    print("\nChoose an option:")
    print("> Choose location (1)")
    print("> Location help (2)")
    print("> Concede (3)")

  # This returns a location on the board (the index, not grid #)
  def getLocation(self):
    # Initialize needed variables
    user_loc = 0
    # Validate data
    while (not(user_loc in (1, 2, 3, 4, 5, 6, 7, 8, 9) or user_loc == -1)):
      try:
        user_loc = int(input("\nSelect a location, -1 to quit: "))
      except ValueError:
        print("Invalid number")
    return user_loc - 1
