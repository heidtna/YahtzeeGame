import random

class Dice:
    def __init__(self, sides):
        """ Description: Constructor
            Precondition: sides is an integer
            Postcondition: Dice attributes are initialized
        """
        self.__sides = sides
        self.__value = 1

    def getValue(self):
        """ Description: Return the value of Dice object
            Precondition: None
            Postcondition: None
        """
        return self.__value

    def Roll(self):
        """ Description: Randomly generate value for Dice object
                         based on the number of sides
            Precondition: None
            Postcondition: value attribute is updated
        """
        self.__value = random.randrange(1, self.__sides+1)