from Dice import Dice

class Yahtzee:

    def __init__(self, playerList):
        """ Description: Constructor
            Precondition: playerList is list of Player objects
            Postcondition: Yahtzee attributes are initialized
        """
        self.__players = [player for player in playerList]
        self.__turns = 0
        self.__dice = [Dice(6) for i in range(5)]

    def getPlayers(self):
        """ Description: Return the list of Players
            Precondition: None
            Postcondition: None
        """
        return self.__players

    def getTurns(self):
        """ Description: Return the number of turns passed
            Precondition: None
            Postcondition: None
        """
        return self.__turns

    def getDice(self):
        """ Description: Return the list of Dice
            Precondition: None
            Postcondition: None
        """
        return self.__dice
    
    def rollDice(self):
        """ Description: Roll each dice in list attribute
            Precondition: None
            Postconition: Dice list attribute is updated
        """
        for dice in self.__dice: dice.Roll()

    def isAces(self):
        """ Description: Evaluate if dice values qualify for 
                         'Aces' category
            Precondition: None
            Postcondition: None
        """
        if 1 in [dice.value for dice in self.__dice]: return True
        else: return False

    def isTwos(self):
        """ Description: Evaluate if dice values qualify for 
                         'Twos' category
            Precondition: None
            Postcondition: None
        """
        if 2 in [dice.value for dice in self.__dice]: return True
        else: return False

    def isThrees(self):
        """ Description: Evaluate if dice values qualify for 
                         'Threes' category
            Precondition: None
            Postcondition: None
        """
        if 3 in [dice.value for dice in self.__dice]: return True
        else: return False

    def isFours(self):
        """ Description: Evaluate if dice values qualify for 
                         'Fours' category
            Precondition: None
            Postcondition: None
        """
        if 4 in [dice.value for dice in self.__dice]: return True
        else: return False

    def isFives(self):
        """ Description: Evaluate if dice values qualify for 
                         'Fives' category
            Precondition: None
            Postcondition: None
        """
        if 5 in [dice.value for dice in self.__dice]: return True
        else: return False

    def isSixes(self):
        """ Description: Evaluate if dice values qualify for 
                         'Sixes' category
            Precondition: None
            Postcondition: None
        """
        if 6 in [dice.value for dice in self.__dice]: return True
        else: return False
    

class Player:

    def __init__(self, name):
        """ Desciption: Constructor
            Precondition: name is a string
            Postcondition: Player attributes are initialized
        """
        self.__name = name
        self.__card = ScoreCard()
        self.__rollNumber = 0

    def setName(self, newName):
        """ Description: Update the name attribute
            Precondition: newName is a string
            Postcondition: name attribute is updated
        """
        self.__name = newName

    def roll(self, diceToRoll=[1,2,3,4,5]):
        """ Description: Roll specific dice based on paramter list
            Precondition: diceToRoll is a list of integers, and each
                          value is unique and the length of the list
                          cannot exceed 5 (the number of dice in Yahtzee)
            Postcondition: Dice values in Yahtzee class are updated
        """

        # A Player can only roll three times per turn
        if self.__rollNumber < 3:
            for dice in diceToRoll:
                Yahtzee.rollDice(dice)
            self.__rollNumber += 1
        else:
            print("Roll limit reached")

class ScoreCard:

    def __init__(self):
        """ Description: Constructor
            Precondition: None
            Postcondition: ScoreCard attributes are initialized
        """
        self.__upperValues = {
            "Aces": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Upper Bonus": -1
        }

        self.__lowerValues = {
            "Three of a Kind": -1,
            "Four of a Kind": -1,
            "Small Straight": -1,
            "Large Straight": -1,
            "Full House": -1,
            "Yahtzee": -1,
            "Yahtzee Bonus": -1
        }

        self.__upperTotal = 0
        self.__lowerTotal = 0
        self.__grandTotal = 0

    def scoreAces(self, roll):
        """ Description: Set value for 'Aces' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Aces' category is set
        """
        self.__upperValues["Aces"] = 1 * roll.count(1)

    def scoreTwos(self, roll):
        """ Description: Set value for 'Twos' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Twos' category is set
        """
        self.__upperValues["Twos"] = 2 * roll.count(2)

    def scoreThrees(self, roll):
        """ Description: Set value for 'Threes' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Threes' category is set
        """
        self.__upperValues["Threes"] = 3 * roll.count(3)

    def scoreFours(self, roll):
        """ Description: Set value for 'Fours' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Fours' category is set
        """
        self.__upperValues["Fours"] = 4 * roll.count(4)

    def scoreFives(self, roll):
        """ Description: Set value for 'Fives' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Fives' category is set
        """
        self.__upperValues["Fives"] = 5 * roll.count(5)

    def scoreSixes(self, roll):
        """ Description: Set value for 'Sixes' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Sixes' category is set
        """
        self.__upperValues["Sixes"] = 6 * roll.count(5)

    def scoreThreeOfAKind(self):
        """ Description: Set value for 'Three of a Kind' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Three of a Kind' category is set
        """
        if (Yahtzee.isThreeOfAKind()):
            self.__lowerValues["Three of a Kind"] = sum(Yahtzee.getDice())
        else:
            self.__lowerValues["Three of a Kind"] = 0

    def scoreFourOfAKind(self):
        """ Description: Set value for 'Four of a Kind' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Four of a Kind' category is set
        """
        if (Yahtzee.isFourOfAKind()):
            self.__lowerValues["Four of a Kind"] = sum(Yahtzee.getDice())
        else:
            self.__lowerValues["Four of a Kind"] = 0

    def scoreYahtzee(self):
        """ Description: Set value for 'Yahtzee' category
            Precondition: roll is a list of integers
            Postcondition: A value for 'Yahtzee' category is set
        """

        # Needs to score Yahtzee Bonus where appropriate:
        #   50 if Yahtzee is already scored
        #   0 if Yatzee is scored as 0
        if (Yahtzee.isYahtzee() ):
            self.__lowerValues["Yahtzee"] = 50
        else:
            self.__lowerValues["Yahtzee"] = 0