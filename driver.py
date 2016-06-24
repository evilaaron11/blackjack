from Deck import *
from Game import *
import sys

BANK = 1000

def main():
   deck = Deck()
   betPlaced = False
   bet = None

   print "******Welcome to Blackjack**********"
   print "*Press \'h\' to hit and \'s\' to stand**"
   print "***To quit at any time, press \'q\'***\n"
   print "\n*****You have $" + str(BANK) + " in the Bank*****\n"
   currGame = Game(deck, BANK)
   #currGame.deck.printCards()

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
               betPlaced = True
            except ValueError,r:
               print str(r)
               continue

         print
      
      currGame.printHand()
      #if currGame.checkIfWon(beforeHouse):
         #return
      print "The dealers top card is a " + str(currGame.house[0])
      inProgress = True 

      while inProgress:
         didSplit = False
         beforeHouse = True
         score = currGame.checkHand(currGame.player)
         print "Current hand: " + str(score)
         if currGame.checkBust(score):
            print "You have busted. You lose."
            currGame.playerBank -= int(bet)
            inProgress = False
            continue
         elif currGame.checkIfWon(beforeHouse):
            currGame.runHouse()
            inProgress = False
            continue
         if currGame.checkIfCanSplit():
            print "You can now split by typing \'sp\'"
            canSplit = True
         else:
            canSplit = False

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
         elif input == "sp" and canSplit:
            #put code here
            print "Not implemented yet"
            didSplit = True
         else:
            print "Invalid input"

         print
      bank = currGame.playerBank
      print "Your current bank has $" + str(bank)
      if bank == 0:
         print "You don\'t have money left in the bank. You lose"
         return
      betPlaced = False
	  #deck = None
      deck = Deck()
      currGame = Game(deck, bank)

if __name__ == "__main__": main()
