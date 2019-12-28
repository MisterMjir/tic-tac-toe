'''
Board Class
-----------
Handles all the logic for the board.
It is mainly used by the game class so it can work. (I really don't know what else to say here)
-----------
-1 = empty
0 = O
1 = X
This is because setting the location to turn % 2 is much easier than manipulating the variables to get 1 and 2
-----------
Gird = The board with numbers of the locations on the board
Board = The physical board with Xs and Os
'''
class Board:
  # Constructor
  def __init__(self):
    # Make the board and make it empty
    self.board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    # Multi-dimension list with all the possible victories (I think)
    self.__wins = [[0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
  # Show the grid
  def showGrid(self):
    gridNum = 0 # Keeps track of the current grid position
    for i in range(5): # Iterate through the rows
      if (i % 2 == 0): # Even rows have numbers (" X ") and walls("|")
        for j in range(5): # Iterate through the columns
          if (j % 2 == 0): # Even columns have numbers (" X ")
            gridNum += 1
            print(" ", gridNum, " ", sep="", end="")
          else: # Odd columns have walls ("|")
            print("|", end="")
      else: # Odd rows just have a floor ("---")
        print("\n--- --- ---")
    print()
    
  # Almost the same as showGrid(), but shows the board
  def showBoard(self):
    gridNum = 0
    for i in range(5):
      if (i % 2 == 0):
        for j in range(5):
          if (j % 2 == 0):
            gridNum += 1
            if (self.board[gridNum - 1] == -1): # -1 prints nothing
              print("   ", end="")
            elif (self.board[gridNum - 1] == 1): # 1 prints X
              print(" X ", end="")
            else: # 0 prints O
              print(" O ", end="")
          else:
            print("|", end="")
      else:
        print("\n--- --- ---")
    print()

  # Figure out if the game has ended
  def isOver(self):
    if (not(-1 in self.board)):
      return 2 # Tie if no one won
    else:
      invalid = [] # Spots where it can't be won
      for combo in range(len(self.__wins)): # Loop through wins
        current = [] # What is currently in the combo
        for spot in range(len(self.__wins[combo])):
          current.append(self.board[self.__wins[combo][spot]])
        if (0 in current and 1 in current):
          invalid.append(combo)
        elif ([0, 0, 0] == current):
          return 0
        elif ([1, 1, 1] == current):
          return 1
    # Delete invalid options
    for i in range(len(invalid)):
      self.__wins.pop(invalid[i]) # Remember that it is not i, but the ith item of invalid
    return -1 # No winner