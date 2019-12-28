'''
AI Class
--------
This is class is used for one player mode,
and it is only on hard diffculty

Also, there is no fancy machine learning for this (that would be cool)
It is just my strategy
'''
class AI():
  def __init__(self, turn):
    self._wins = [[0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8]]
    self.turn = turn
    self.target = self.turn * -1 + 1

  def getSpot(self, board):
    danger = [] # Combos where the opponent can win
    for i in range(self._wins): # Iterate through win combos
      pass
