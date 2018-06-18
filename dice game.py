def gameOver(s1, s2):
    over = False
    if s1>= 100 or s2>=100:
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
    elif die1!=1 and die2!=1:
        points = die1+die2
    return points

def displayWinner(s1,s2):
    if s1>s2:
        print("The winner is player 1: score", s1)
    elif s1<s2:
        print(" The winner is Player 2: score ", s2)
    else:
        print("both players have the same score", s1)
              
def updateScore(score, points):
    if points !=-1:
        score +=points
    else:
        score=0
    return score

score1 = 0
score2 = 0

while not gameOver(score1, score2):
    points = castDice()
    score1 = updateScore(score1, points)
    points = castDice()
    score2 = updateScore(score2, points)
    print("player 1: ", score1, "player 2: ", score2)

displayWinner(score1, score2)
