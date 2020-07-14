from card import Card
from linkedList import LinkedList

class Hand(LinkedList):
    """
    This represents a Player's Hand in the game.
    It inherits from LinkedList - it is a LinkedList.
    The Player holds the Hand as an instance variable.
    The Player controls the Hand calling the LinkedList methods.
    """
    def __init__(self):
        """
        Constructor:
        Calls the LinkedList constructor
        """
        super().__init__()

    def __str__(self):
        """
        Returns a string containing the list of Cards
        in the Hand: 13 Cards to a line
        The newline character is added for every 13th Card.
        """

        hand_str = ""
        current = self._head
        for c in range(len(self)):
            hand_str += "{} ".format(current.data)
            if  (c+1) % 13 == 0:
                hand_str += '\n'
            current = current.next
        return hand_str



