from Deck import *
from Card import *
import time

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
   split = []
   playerBank = 0
   currBet = 0

   def __init__(self, deck, bankVal):
      self.player = []
      self.house = []
      self.playerBank = bankVal
      self.deck = deck
      self.initHand()
      #self.playerBank = 1000 # Default of $1000

   def initHand(self):
      for i in range(0,2):
         self.player.append(self.deck.drawCard())
         self.house.append(self.deck.drawCard())

   def checkHand(self, cards):
      score = 0
      numAces = 0
      for i in cards:
         currVal = str(i.val)
         if currVal.isdigit():
            score += i.val
         elif i.val == "A":
            if MAX_VALUE >= (score + ACE):
               score += ACE
            else:
               score += 1
            numAces += 1
         else:
            score += FACE_VALUE

      while numAces > 0 and score > MAX_SCORE:
         score -= FACE_VALUE
         numAces -= 1

      return score

   def placeBet(self, bet):
      if bet > self.playerBank:
         raise ValueError("Not enough money in the bank")
      else:
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

      while houseScore < HOUSE_STAY and houseScore < playerScore:
         print "House score: " + str(houseScore)
         print
         time.sleep(2)
         print "Dealer took a hit\n"

         self.hitDealer()
         self.printDealer()
         houseScore = self.checkHand(self.house)

      if self.checkIfTied():
         print "You have tied"   
      elif self.checkIfWon(False):
         self.playerBank += self.currBet
         print "You won"
      else:
         self.playerBank -= self.currBet
         print "You lose"

   def checkIfTied(self):
      return self.checkHand(self.player) == self.checkHand(self.house)

   def checkIfCanSplit(self):
      same = False
      if len(self.player) == 2:
         same = (self.player[0].val == self.player[1].val)

      return same

   def doSplit(self):
      tempCard1 = self.player[0]
      tempCard2 = self.player[1]
      self.player = []
      self.player.append(tempCard1)
      self.split.append(tempCard2)


   def checkIfWon(self, beforeHouse):
      playerScore = self.checkHand(self.player)
      houseScore = self.checkHand(self.house)
      if not beforeHouse:
         print "House score: " + str(houseScore)
      if beforeHouse:
         if playerScore == MAX_VALUE:
            print "You have 21"
            print 
            return True
         else:
            return False
      elif self.checkBust(houseScore):
         print "\nThe House has busted"
         return True
      else:
         return playerScore > houseScore


