class Card:
   suit = None
   val = None

   def __init__(self, suit, rank):
      self.suit = suit
      self.val = rank

   def __str__(self):
      return str(self.val) + " of " + self.suit
