from Card import *
import random
#import shuffle

DECK_SIZE = 52
NUM_PER_SUIT = 13
suits = ["Spades","Diamonds","Clubs","Hearts"]

class Deck:
   cards = []

   def __init__(self):
      currCount = 1
      currSuit = suits.pop()
      while len(self.cards) < DECK_SIZE:
         
         if currCount > NUM_PER_SUIT:
            currCount = 1
            currSuit = suits.pop()
         if currCount <= 10:
            if currCount > 1:
               self.cards.append(Card(currSuit, currCount))
            else:
               self.cards.append(Card(currSuit, "A"))
         elif currCount == 11:
            self.cards.append(Card(currSuit, "J"))
         elif currCount == 12:
            self.cards.append(Card(currSuit, "Q"))
         elif currCount == 13:
            self.cards.append(Card(currSuit, "K"))

         currCount = currCount + 1
      random.shuffle(self.cards)

   def drawCard(self):
      return self.cards.pop()

   def printCards(self):
      for i in self.cards:
         print i
