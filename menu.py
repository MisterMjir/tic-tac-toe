'''
Menu Class
----------
Handles the logic for the menu
'''
class Menu:
  # Constructor
  def __init__(self):
    # Print out stuff
    self.showTitle()
    self.showOptions()
    # Allowed option inputs
    self.one_player_opts = ("1", "(1)", "1 player")
    self.two_player_opts = ("2", "(2)", "2 player")

  # Get the title from the file and print it
  def showTitle(self):
    title = open("title.txt", "r")
    title_txt = title.read()
    print(title_txt)

  # Print the options
  def showOptions(self):
    print("Options:")
    print("> 1 Player (1)")
    print("> 2 Player (2)\n")

  # Return the mode that will be sent to the game class
  def getMode(self, mode):
    if (mode in self.one_player_opts): # 1 Player
      print("Sorry, that mode is currently unavailable\n")
      return 0
    elif (mode in self.two_player_opts): # 2 Players
      return 2
    else: # Invalid
      print("The input recieved was invalid\n")
      return 0
  