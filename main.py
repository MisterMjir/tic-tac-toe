from menu import *
from game import *
'''
Hello, this is my tic tac toe program
Everything should be explained in detail in each of the class files
If you were wondering, this is just the file that brings all the classes
together to create some structure, although it is really only for the
menu and game class.
'''
# Menu/Title
menu = Menu()
mode = 0
while(mode == 0):
  mode = menu.getMode(input("Select a mode: "))

# Game
game = Game(mode)
game.run()
