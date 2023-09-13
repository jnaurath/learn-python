import random


dice = [1, 2, 1, 1, 1]
iterations = 0


def checkForYahtzee():
    if dice == [1, 1, 1, 1, 1] or dice == [2, 2, 2, 2, 2] or dice == [3, 3, 3, 3, 3] or dice == [4, 4, 4, 4, 4] or dice == [5, 5, 5, 5, 5] or dice == [6, 6, 6, 6, 6]:
        print("Yahtzee!!!")
        print(dice)
        print(f"after {iterations} iterations")
        return True
    else:
        return False


def rollDice():

    dice[0] = random.randint(1, 6)
    dice[1] = random.randint(1, 6)
    dice[2] = random.randint(1, 6)
    dice[3] = random.randint(1, 6)
    dice[4] = random.randint(1, 6)

    print(dice)


while not checkForYahtzee():
    iterations += 1
    rollDice()
