import random
from card import Card

class Deck(list):
    """
    This class represents a Deck of Cards.
    It inherits from list - it is a list
    Cards are added at the end of the list: Use append
    Cards are dealt from the end of the list: Use pop()
    """

    def __init__(self):
        """
        Constructor:
        Calls the list constructor
        """
        super().__init__()

    def initialize(self):
        """
        Initializes the Deck with 52 Cards
          Both the Suits and Ranks are integers
            Suits: 0=Clubs, 1=Diamonds, 2=Hearts, 3=Spades
            Ranks: 1=Ace, 2-10=2=10, 11=Jacks, 12=Queen, 13=King
        """

        suits = [0, 1, 2, 3]
        for j in suits:
            suit = suits[j]
            for i in range(1,14):
                rank = i
                card = Card(suit, rank)
                self.add_card(card)

    def add_card(self, card):
        """
        Add the Card to the end of the list
        """
        self.append(card)

    def deal(self):
        """
        Removes and returns the last Card in the list
        That's what gamblers call dealing from the bottom of the deck
        """
        return self.pop()

    def shuffle(self):
        """
        The random class has a shuffle method
        that accepts a list as an argument
        Use it to shuffle the Deck
        No return needed
        """
        random.shuffle(self)

    def __str__(self):
        """
        Returns a string containing the list of Cards
        in the Deck: 13 Cards to a line
        The newline character is added for every 13th Card
        """

        deck_str = ""
        i = 0
        for c in self:
            deck_str += "{} ".format(c)
            i +=1
            if i == 13:
                deck_str += '\n'
                i = 0

        return deck_str

