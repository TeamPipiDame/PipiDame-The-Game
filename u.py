import random

def chooseComputerMove():

    #This just fills a list with all the empty boxes and chooses one at random
    emptyBoxes = []
    for i in range(0, 3):
        for j in range(0, 3):
            if (boxes[i][j] == 0):
                emptyBoxes += [[i, j]]

    return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]

 # Make the computer's move
    computerMove = chooseComputerMove()
    boxes[computerMove[0]][computerMove[1]] = 1
    print('\n' 'Computer\'s turn:')
    printGrid()

    # Check if the computer's move won the game
    victoryResult = checkVictory()
    if (victoryResult == 'O'):
        print ('Computer wins!')
        break
