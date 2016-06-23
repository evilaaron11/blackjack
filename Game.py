from Deck import *
from Card import *

# Constants
FACE_VALUE = 10
ACE = 11
MAX_VALUE = 21

class Game:
   # Variables to keep track of current deck and hands
   deck = None
   player = []
   house = []

   def __init__(self, deck):
      self.deck = deck
      self.initHand()

   def initHand(self):
      for i in range(0,2):
         self.player.append(self.deck.drawCard())
         self.house.append(self.deck.drawCard())

   def checkHand(cards):
      score = 0
      for i in cards:
         if cards.val.isdigit():
            score += cards.val
         elif cards.val == "A":
            if MAX_VALUE > score + ACE:
               score += ACE
            else:
               score += 1
         else:
            score += FACE_VALUE

      return score

   def hitMe(self):
      self.player.append(self.deck.drawCard())

   def checkBust(score):
      return score > MAX_VALUE

   def printHand(self):
      for i in self.player:
         print i

   #run AI
   def runHouse(self):
      print "Not yet implemented"
