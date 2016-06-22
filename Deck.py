from Card import *
import random
#import shuffle

class Deck:
   cards = []
   DECK_SIZE = 52
   NUM_PER_SUIT = 13
   suits = ["Spades","Diamonds","Clubs","Hearts"]

   def __init__(self):
      currCount = 1
      currSuit = self.suits.pop()
      while len(self.cards) < self.DECK_SIZE:
         
         if currCount > self.NUM_PER_SUIT:
            currCount = 1
            currSuit = self.suits.pop()
         if currCount <= 10:
            self.cards.append(Card(currSuit, currCount))
         elif currCount == 11:
            self.cards.append(Card(currSuit, "J"))
         elif currCount == 12:
            self.cards.append(Card(currSuit, "Q"))
         elif currCount == 13:
            self.cards.append(Card(currSuit, "K"))

         currCount = currCount + 1
      random.shuffle(self.cards)

   def printCards(self):
      for i in self.cards:
         print i
