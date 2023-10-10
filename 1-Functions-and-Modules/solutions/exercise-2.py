import random

userNumbers = []
wonLottery = False
WINNING_NUMBERS = 6
NUMBER_RANGE = 49
iterations = 0
printFrequency = 1000000

sum = 0
price = 1.4
wins = [
    0,
    0,
    0,
    12.8,
    64.1,
    6169.3,
    758234.7,
]
userInput = True


def checkNumberValid(inputNumbers, newNumber):
    if newNumber not in range(1, NUMBER_RANGE+1):
        return False
    if newNumber in inputNumbers:
        return False
    return True


def getUserNumbers():
    for i in range(WINNING_NUMBERS):
        if userInput:
            newNumber = int(input(f"Number {i+1}:"))
            while not checkNumberValid(userNumbers, newNumber):
                newNumber = int(input(f"Number {i+1}:"))
                checkNumberValid(userNumbers, newNumber)
            userNumbers.append(newNumber)
        else:
            randomNumber = random.randint(1, NUMBER_RANGE)
            while not checkNumberValid(userNumbers, randomNumber):
                randomNumber = random.randint(1, NUMBER_RANGE)
                checkNumberValid(userNumbers, randomNumber)
            userNumbers.append(randomNumber)


def checkForWin(lotteryNumbers, userNumbers):
    global sum
    global iterations
    iterations += 1
    lotteryNumbers.sort()
    userNumbers.sort()

    correctNumbers = 0
    for i in lotteryNumbers:    # 1,2,3,4,5,6
        if i in userNumbers:    # 5,6,7,8,9,10
            correctNumbers += 1
    sum -= price + wins[correctNumbers]

    if iterations % printFrequency == 0:
        print(f"{iterations} Iterations, Balance: {round(sum, 2)}")
        print(userNumbers)
        print(lotteryNumbers)
    if lotteryNumbers == userNumbers:
        print("won", lotteryNumbers, userNumbers)
        print(iterations, round(sum, 2))
        return True
    else:
        return False


def playLottery():
    lotteryNumbers = []
    for i in range(WINNING_NUMBERS):
        randomNumber = random.randint(1, NUMBER_RANGE)
        while not checkNumberValid(lotteryNumbers, randomNumber):
            randomNumber = random.randint(1, NUMBER_RANGE)
            checkNumberValid(lotteryNumbers, randomNumber)
        lotteryNumbers.append(randomNumber)
    return checkForWin(lotteryNumbers, userNumbers)


getUserNumbers()
while not wonLottery:
    wonLottery = playLottery()
