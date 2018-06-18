class Die:
    def __init__(self):
        self._Value = 1 
        
    def GetDieValue(self):
        return self._Value
    
    def RollDie(self):
        import random
        dice = random.randint(1,6)
        self._Value = dice
        
    
    
class Player:
    def __init__(self, name):
        self._name = name 
        self._score = 0 
        
    def UpdateScore(self, points):
        self._score += points
    
    def ResetScore(self):
        self._score = 0 
    


playerOne = Player("josh")
playerTwo = Player("Lucy")
playerOne.ResetScore()
playerTwo.ResetScore()
DiceOne = Die()
DiceTwo = Die()
DiceOne.RollDie()
TotalOne = DiceOne.GetDieValue()
DiceTwo.RollDie()
TotalOne += DiceTwo.GetDieValue()
playerOne.UpdateScore(TotalOne)
DiceOne.RollDie()
TotalTwo = DiceOne.GetDieValue()
DiceTwo.RollDie()
TotalTwo += DiceTwo.GetDieValue()
playerOne.UpdateScore(TotalTwo)
print("Player One Score: ", TotalOne)
print("Player Two Score: ", TotalTwo)
if TotalOne < TotalTwo:
    print("Player Two with score: ", TotalTwo, " wins")
else:
    print("Player One with score: ", TotalOne," wins") 


