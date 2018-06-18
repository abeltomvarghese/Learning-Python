def gameOver(ScoreList):
    over = False
    for k in range(numOfP): 
        if ScoreList[k] >= 100: 
            over = True
    return over

def castDice():
    import random
    die1 = random.randint(1,6)
    die2= random.randint(1,6)
    points=0
    print("die 1-->", die1, "Die2 -->", die2)
    if die1==1 and die2==1:
        points=-1
    elif die1!=1 or die2!=1:
        points = die1+die2
    return points

def displayWinner(ListOfScores):
    winnerScores = 0

    for s in range(numOfP): 
         
        if ListOfScores[s] > winnerScores:
            winnerScores = ListOfScores[s]
            PlayerNum = s
    print("Player ",PlayerNum, " has won with: ", winnerScores)        
    
              
def updateScore(score, points):
    if points !=-1:
        score +=points
    else:
        score=0
    return score

playAgain = "Yes"
while playAgain == "Yes":
    numOfP = int(input("Enter the number of players"))
    
    Scores = []
    for x in range(numOfP):
        Scores.append(0)

    while not gameOver(Scores):
        for y in range(numOfP):
            points = castDice()
            score = updateScore(Scores[y],points)
            Scores[y] = score
            print("Player ", y,":",Scores[y]) 
    
    
    displayWinner(Scores)
    playAgain = input("Play Again? ")
    
