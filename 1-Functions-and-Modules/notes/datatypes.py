tictactoe = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

PLAYER_1 = "x"
PLAYER_2 = "0"


def printGame(tictactoe):
    for i in range(len(tictactoe)):
        print(tictactoe[i])
    print()
    print()


# game start
allowedUserInput = [PLAYER_1, PLAYER_2]


def changePlayer():
    global currentPlayer
    if currentPlayer == PLAYER_1:
        currentPlayer = PLAYER_2
    elif currentPlayer == PLAYER_2:
        currentPlayer = PLAYER_1


def nextMove(tictactoe, x, y, userInput):
    if userInput in allowedUserInput:
        if not tictactoe[x][y] == " ":
            print("Not allowed")
        else:
            tictactoe[x][y] = userInput
    else:
        print("Invalid input")
    printGame(tictactoe)
    changePlayer()
    return tictactoe


printGame(tictactoe)
currentPlayer = PLAYER_1
nextMove(tictactoe, 0, 0, currentPlayer)
nextMove(tictactoe, 1, 1, currentPlayer)
nextMove(tictactoe, 2, 2, currentPlayer)
nextMove(tictactoe, 0, 1, currentPlayer)
nextMove(tictactoe, 2, 0, currentPlayer)
nextMove(tictactoe, 2, 1, currentPlayer)


matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

matrix3 = [
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ],
    [
        [1, 0, 0],
        [0, 1, 5],
        [0, 0, 1],
    ],
]
