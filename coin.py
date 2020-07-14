from random import randint
class Coin:
    """
    This class represents a Coin that is flipped
    returning 1 for 'Heads' and 0 for 'Tails'
    """
    def __init__(self):
        """
        Constructor:
        Instance variable: face holds 'Heads' or 'Tails'
        Use random randint to randomly return
            1 for 'Heads' and 0 for 'Tails'
        """

        num = randint(0,1)
        if num == 1:
            self.__face = 'Heads'
        else:
            self.__face = 'Tails'

    def flip(self):
        """
        Use random randint to randomly return
           1 for 'Heads' and 0 for 'Tails'
        """

        num = randint(0,1)
        if num == 1:
            self.__face = 'Heads'
        else:
            self.__face = 'Tails'
        return self.__face

    def __str__(self):
        """
        Returns the face: 'Heads' or 'Tails'
        """

        return self.__face
