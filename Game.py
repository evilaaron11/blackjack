from Deck import *
from Card import *

# Constants
FACE_VALUE = 10
ACE = 11
MAX_VALUE = 21

class Game:
   # Variables to keep track of current deck and hands
   deck = None
   player = None
   house = None

   def __init__(self, deck):
      self.deck = deck
      self.initHand()

   def initHand(self):
      for i in 2:
         player = self.deck.drawCard()
         house = self.deck.drawCards()

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

   def checkBust(score):
      return score > MAX_VALUE
