__author__ = "D. Brown"

def makeGrid():
    """returns a 2 dimensional list to be used as a grid for this program.
    """
    return [[0 for column in range(3)] for row in range(3)]

# Doctest
def drawGrid(currentGrid):
    """
        creates and then returns the grid in a string format

        Takes each row and creates the columns needed from counting the rows and columns in the parameter currentGrid. This
        is then added along with the table-headings to a string variable and returns the complete grid in string format

        >>> drawGrid([[0,0,0],[0,0,0],[0,0,0]])
        '  0 1 2\\n0 - - - \\n1 - - - \\n2 - - - \\n'

        >>> drawGrid([[1,0,0],[0,2,0],[0,0,1]])
        '  0 1 2\\n0 X - - \\n1 - O - \\n2 - - X \\n'

        >>> drawGrid([[1,1,1],[2,2,2],[1,1,1]])
        '  0 1 2\\n0 X X X \\n1 O O O \\n2 X X X \\n'

    """
    gridContent = "  0 1 2\n"
    for rowNumber in range(len(currentGrid)):
        gridContent += str(rowNumber) + " "
        for eachColumn in range(len(currentGrid[rowNumber])):
            if currentGrid[rowNumber][eachColumn] == 1:
                gridContent += "X "
            elif currentGrid[rowNumber][eachColumn] == 2:
                gridContent += "O "
            else:
                gridContent += "- "
        gridContent += "\n"
    return gridContent


def emptyCellCheck(currentGrid, row, column):
    """returns whether the required cell is empty using row and column to search in currentGrid"""
    return currentGrid[row][column] > 0
    
def enterP1Move(currentGrid, row, column):
    """enters Player 1 move into currentGrid using row and column to access that particular cell"""
    currentGrid[row][column] = 1
    
def enterP2Move(currentGrid, row, column):
    """enters Player 2 move into currentGrid using row and column to access that particular cell"""
    currentGrid[row][column] = 2

# Doctest
def chkDiagonalWin(currentGrid):
    """returns the player number of player who has won the game diagonally by checking currentGrid

    Checks the centre cell in currentGrid to see if which player has made a move there and whether they have made marks
    in any corners of the grid as well. The player number who has scored three marks diagonally is returned.

    >>> chkDiagonalWin([[0,0,0],[0,1,0],[0,0,0]])
    -1

    >>> chkDiagonalWin([[1,0,0],[0,1,0],[0,0,1]])
    1

    >>> chkDiagonalWin([[0,0,2],[0,2,0],[2,0,0]])
    2

    >>> chkDiagonalWin([[1,0,0],[0,2,0],[0,0,1]])
    -1
    """
    centreCell = currentGrid[1][1]
    if centreCell > 0 and ((currentGrid[0][0] == centreCell and currentGrid[2][2] == centreCell) or (currentGrid[2][0] == centreCell and currentGrid[0][2] == centreCell)):
        winnerNum = centreCell
    else:
        winnerNum = -1
    return winnerNum

# Doctest
def chkGameWon(currentGrid):
    """returns the player number who has won the game either horizontally or vertically using the contents of currentGrid.

    checks to see how many times a player has made a mark in each row and column of currentGrid. When this happens three times the player's
    number is returned. If no one was able to win, value zero is returned to indicate game ended in a draw.

    >>> chkGameWon([[0,2,0],[0,1,0],[0,0,0]])
    -1
    >>> chkGameWon([[2,2,2],[1,1,0],[0,0,1]])
    2
    >>> chkGameWon([[2,1,1],[2,1,0],[2,0,1]])
    2
    >>> chkGameWon([[2,1,1],[0,1,1],[2,0,1]])
    1
    >>> chkGameWon([[2,1,1],[2,1,0],[1,1,1]])
    1
    >>> chkGameWon([[1,0,0],[0,1,0],[0,0,1]])
    1
    >>> chkGameWon([[0,0,2],[0,2,0],[2,0,0]])
    2
    """
    drawCounter = 0
    winnerNum = chkDiagonalWin(currentGrid)
    rowNum = 0

    p1VerticalCells = [0, 0, 0]
    p2VerticalCells = [0, 0, 0]
    
    while winnerNum < 0 and rowNum < len(currentGrid):
        p1HCount = 0
        p2HCount = 0
        columnNum = 0
        while winnerNum < 0 and columnNum < len(currentGrid[rowNum]):
            if currentGrid[rowNum][columnNum] == 1:
                p1HCount += 1
                p1VerticalCells[columnNum] += 1
                if p1VerticalCells[columnNum] == 3:
                    winnerNum = 1
            elif currentGrid[rowNum][columnNum] == 2:
                p2HCount += 1
                p2VerticalCells[columnNum] += 1
                if p2VerticalCells[columnNum] == 3:
                    winnerNum = 2
            columnNum += 1
        
        if p1HCount == 3:
            winnerNum = 1             # here is the bug..... change from 2 to a 1!!!
        elif p2HCount == 3:
            winnerNum = 2
        elif p1HCount + p2HCount == 3:
            drawCounter += 1

        rowNum += 1
    
    if drawCounter == 3:
        winnerNum = 0
    return winnerNum

def getNextPlayer(currentPlayer):
    """returns the next player's number using the value stored in currentPlayer parameter"""
    return 2 - currentPlayer + 1
    
def startGame():
    """Manages the game simulation

    Takes in and checks the user input is valid. Then enters the mark and displays the grid while checking whether the
    game has been won yet.  """
    currentGrid = makeGrid()
    playerNum = 2
    winnerNum = -1
    print(drawGrid(currentGrid))
    while winnerNum < 0:
        playerNum = getNextPlayer(playerNum)
        if playerNum == 1:
            print("X's turn")
        elif playerNum == 2:
            print("O's turn")
              
        invalidMove = True
        while invalidMove:
            xCoord = -1
            while xCoord < 0 or xCoord > 2:
                validRNum = input("Enter row: ")
                if validRNum.isdigit():
                    xCoord = int(validRNum)
                    if xCoord < 0 or xCoord > 2:
                        print("The input must be between 0 and 2 inclusive\n")
                else:
                    print("The input must be a number\n")
                          
            yCoord = -1
            while yCoord < 0 or yCoord > 2:
                validColumn = input("Enter column: ")
                if validColumn.isdigit():
                    yCoord = int(validColumn)
                    if yCoord < 0 or yCoord > 2:
                        print("The input must be between 0 and 2 inclusive\n")
                else:
                    print("The input must be a number\n")

            invalidMove = emptyCellCheck(currentGrid, xCoord, yCoord)
            if invalidMove:
                print("Position already played\n")
        
        if playerNum == 1:
            enterP1Move(currentGrid, xCoord, yCoord)
        elif playerNum == 2:
            enterP2Move(currentGrid, xCoord, yCoord)

        winnerNum = chkGameWon(currentGrid)
        print()
        print(drawGrid(currentGrid))

    if winnerNum == 1:
        print("X wins!")
    elif winnerNum == 2:
        print("O wins!")
    else:
        print("Draw!")    

if __name__ == "__main__":
    startGame()
