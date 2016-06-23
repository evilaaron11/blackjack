from Deck import *
from Card import *

# Constants
FACE_VALUE = 10
ACE = 11
MAX_VALUE = 21
HOUSE_STAY = 17

class Game:
   # Variables to keep track of current deck and hands
   deck = None
   player = []
   house = []
   playerBank = None
   currBet = 0

   def __init__(self, deck):
      self.deck = deck
      self.initHand()
      self.playerBank = 1000 # Default of $1000

   def initHand(self):
      for i in range(0,2):
         self.player.append(self.deck.drawCard())
         self.house.append(self.deck.drawCard())

   def checkHand(self, cards):
      score = 0
      for i in cards:
         currVal = str(i.val)
         if currVal.isdigit():
            score += i.val
         elif i.val == "A":
            if MAX_VALUE > score + ACE:
               score += ACE
            else:
               score += 1
         else:
            score += FACE_VALUE

      return score

   def placeBet(self, bet):
      if bet > self.playerBank:
         raise ValueError("Not enough money in the bank")
      else:
         self.playerBank -= bet
         self.currBet = bet

   def hitMe(self):
      self.player.append(self.deck.drawCard())

   def hitDealer(self):
      self.house.append(self.deck.drawCard())

   def checkBust(self, score):
      return score > MAX_VALUE

   def printHand(self):
      for i in self.player:
         print i

   def printDealer(self):
      for j in self.house:
         print j

   #run AI
   def runHouse(self):
      print "Houses\'s turn:"
      self.printDealer()

      playerScore = self.checkHand(self.player)
      houseScore = self.checkHand(self.house)

      while houseScore < HOUSE_STAY:
         print "House score: " + str(houseScore)
         print
         print "Dealer took a hit\n"

         self.hitDealer()
         self.printDealer()
         houseScore = self.checkHand(self.house)

      if self.checkIfWon(False):
         self.playerBank += self.currBet
         print "You won"
      else:
         print "You lose"

   def checkIfWon(self, beforeHouse):
      playerScore = self.checkHand(self.player)
      houseScore = self.checkHand(self.house)

      if beforeHouse:
         if playerScore == MAX_VALUE:
            print "You have 21"
            return True
         else:
            return False
      elif self.checkBust(houseScore):
         return True
      else:
         return playerScore > houseScore


