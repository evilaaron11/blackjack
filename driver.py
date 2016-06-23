from Deck import *
from Game import *
import sys

def main():
   beforeHouse = True
   deck = Deck()
   betPlaced = False
   bet = None

   print "******Welcome to Blackjack**********"
   print "**Press \'h\' to hit and \'s\' to stay**"
   print "***To quit at any time, press \'q\'***\n"

   currGame = Game(deck)

   while True:
      while not betPlaced:
         bet = raw_input("Place your bet: ")
         if bet == "q":
            return
         elif not str(bet).isdigit():
            print "Please enter a valid number"
         else:
            try:
               currGame.placeBet(int(bet))
            except ValueError,r:
               print str(r)
               continue

         betPlaced = True
         print
      
      currGame.printHand()
      #if currGame.checkIfWon(beforeHouse):
         #return
      print "The dealers top card is a " + str(currGame.house[0])
      inProgress = True 

      while inProgress:

         score = currGame.checkHand(currGame.player)
         print "Current hand: " + str(score)
         if currGame.checkBust(score):
            print "You have busted. You lose."
            inProgress = False
         elif currGame.checkIfWon(beforeHouse):
            currGame.runHouse()
            inProgress = False

         print
         input = raw_input()
         print
         if input == "q":
            inProgress = False
            return
         elif input == "h":
            currGame.hitMe()
            currGame.printHand()
         elif input == "s":
            currGame.runHouse()
            beforeHouse = False
            inProgress = False
         else:
            print "Invalid input"

         print
      print "Your current bank has $" + str(currGame.playerBank)
      betPlaced = False
	  #deck = None
      deck = Deck()
      currGame = Game(deck)

if __name__ == "__main__": main()
