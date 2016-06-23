from Deck import *
from Game import *
import sys

def main():
   beforeHouse = True
   deck = Deck()
   inProgress = True

   print "******Welcome to Blackjack**********"
   print "**Press \'h\' to hit and \'s\' to stay**"
   print "***To quit at any time, press \'q\'***\n"
   
   currGame = Game(deck)
   currGame.printHand()
   
   if currGame.checkIfWon(beforeHouse):
      return
   print "The dealers top card is a " + str(currGame.house[0])
   
   while inProgress:
      score = currGame.checkHand(currGame.player)
      print "Current hand: " + str(score)
      if currGame.checkBust(score):
         print "You have busted. You lose."
         break
      elif currGame.checkIfWon(beforeHouse):
         currGame.runHouse()
         break
      
      print
      input = raw_input()
      print
      if input == "q":
         inProgress = False
      elif input == "h":
         currGame.hitMe()
         currGame.printHand()
      elif input == "s": 
         currGame.runHouse()
         beforeHouse = False
         break
      else:
         print "Invalid input"

      print

if __name__ == "__main__": main()
