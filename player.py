from hand import Hand
from pile import Pile

class Player:
    """
    This class represents a Player of the game
    The Player holds his Hand as an instance variable,
    The Hand is a LinkedList of Cards.
    When a Player is dealt a Card from the Deck, the Card is
       added first in his Hand
    When a Player adds a Pile after becoming the winner, the Pile
       of Cards is added last to the Hand, one at a time
    Cards are only played from the front of the Hand
    """
    def __init__(self):
        """
        Constructor:
        Creates the empty hand
        """
        self.__pile = Pile()
        self.__hand = Hand()

    def add_card(self, card):
        """
        Add the passed in Card to the Hand at the front
        Working from broker while dealing
        """
        self.__hand.add_first(card)

    def add_pile(self, pile):
        """
        Add the passed in Pile of Cards to the Hand at the back.
        The Cards are removed from the Pile and added to the Hand
        - one at a time
        """
        for i in range(len(pile)):
            card = pile.remove_first()
            self.__hand.add_last(card)

    def play_card(self, pile):
        """
        Remove the top Card from the Hand
        And add it to the passed in Pile
        Use a method from the Pile class
        """
        card = self.__hand.remove_first()
        pile.add_card(card)

    def get_num_cards(self):
        """
        Return the number of Cards in the Hand
        """
        return len(self.__hand)

    def display_hand(self):
        """
        Display the Player's Hand by calling the __str__ method
        """
        print(self.__hand.__str__())

