from card import Card
from linkedList import LinkedList

class Pile(LinkedList):
    """
    This class represents a Pile of Cards on the table.
    It inherits from LinkedList - it is a LinkedList.
    The Cards are added and removed at the front of the Pile.
    """
    def __init__(self):
        """
        Constructor:
        Calls the LinkedList constructor.
        """
        super().__init__()


    def add_card(self, card):
        """
        Adds the Card to the front of the list
        """
        self.add_first(card)

    def remove_card(self):
        """
        Removes and returns the Card at the front of the list
        """
        return self.remove_first()

    def top_two_cards(self):
        """
        Retrieves the 1st two nodes and returns the Cards
        Return Player1 Card, Player2 Card:
               Watch out for the correct order
        """
        current = self._head
        player1card = current.data
        player2card = current.next.data
        return player2card, player1card

    def __str__(self):
        """
        Returns the Cards in the Pile as a string by calling the
        __str__ method of the Card object, starting with the first
        Card as:  Rank-Suit Rank-Suit Rank-Suit etc
        """

        pile_str = ""
        current = self._head
        for c in range(len(self)):
            pile_str += "{} ".format(current.data)
            current = current.next
        return pile_str


