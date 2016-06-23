from Deck import *
from Game import *
import sys

def main():
   deck = Deck()
   #deck.printCards()
   inProgress = True
   print "Welcome to Blackjack"
   print "Press \'h\' to hit and \'s\' to stay"
   print "To quit at any time, press \'q\'"
   currGame = Game(deck)
   currGame.printHand()
   
   while inProgress:
      input = raw_input()
      if input == "q":
         inProgress = False
      elif input == "h":
         currGame.hitMe()
         currGame.printHand()
      elif input == "s":
         currGame.runHouse()
      else:
         print "Invalid input"

      

if __name__ == "__main__": main()
