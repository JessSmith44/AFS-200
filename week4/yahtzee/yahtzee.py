import random

class Die:
    def __init__(self, face: int = None, sides=6):
        self.sides = sides
        self.__face = face

    def __str__(self):
        return str(self.__face)

    def roll(self):
        value = random.randint(1, self.sides)
        self.__face = value
    
    def getCurrentFaceValue(self):
        return self.__face

    def showDieFace(self):
        print(self.__face)

def main():
    my_die1 = Die()
    my_die2 = Die()
    my_die3 = Die()
    my_die4 = Die()
    my_die5 = Die()
    my_die1.roll()
    my_die2.roll()
    my_die3.roll()
    my_die4.roll()
    my_die5.roll()
    print("(" + str(my_die1.getCurrentFaceValue()) + ")", "(" + str(my_die2.getCurrentFaceValue()) + ")", "(" + str(my_die3.getCurrentFaceValue()) + ")", "(" + str(my_die4.getCurrentFaceValue()) + ")", "(" + str(my_die5.getCurrentFaceValue()) + ")")
    dice_list = [my_die1, my_die2, my_die3, my_die4, my_die5]
    check_yahtzee(dice_list)

def check_yahtzee(dice_list):
    myCounter = 1
    for index in range(0, len(dice_list) -1):
        if dice_list[index].getCurrentFaceValue() == dice_list[index + 1].getCurrentFaceValue():
            myCounter +=1
    if len(dice_list) == myCounter:
        print("Yahtzee!")
    else:
        return False
    # below at 100 for testing for a yahtzee should be one
for index in range(0, 1):
    main()



