#question 3(a),(b)
class Card:
    def __init__(self,CNum, CColour):
        self.__CNum  = CNum
        self.__CColour = CColour
    
    def GetNumber(self):
        return self.__CNum
    
    def GetColour(self):
        return self.__CColour
    
    
#MAIN PROGRAM, question 3(c)
cardsArray = [None for _ in range(30)]

try: 
    file = open("/workspaces/school/google classroom/9618_s22_qp_42 files/CardValues.txt", 'r')
    for i in range(30):
        numRead = int(file.readline())
        colourRead = file.readline()
        cardsArray[i] = Card(numRead,colourRead)
    file.close()
except FileNotFoundError:
    print("Sorry, file does not exist!")

#question 3(d)
chosenArray = [False for i in range(30)]
def ChooseCard():
    continueFlag = True
    while continueFlag == True:
        index = int(input("Please enter a valid index between 1 and 30 inclusive:"))
        if index < 1 and index > 30:
            index = int(input("Please enter a valid index between 1 and 30 inclusive:"))
        elif chosenArray[index-1] == True:
            print("Card is unavailable, please choose a different card!")
        else:
            print("Card was successfully chosen!")
            continueFlag = False
    chosenArray[index-1] = True
    return index-1

Player1 = [] #of Card, 4 elements
for i in range(4):
    Player1.append(cardsArray[ChooseCard()])
for i in range(4):
    print(Card.GetNumber(Player1[i]))
    print(Card.GetColour(Player1[i]))
