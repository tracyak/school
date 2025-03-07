#google classroom, task 2

#question 1(a)
PlayerArray = [[None,None] for _ in range(11)] #global string, 11 by 2 elements

#question 1(b)
def ReadHighScores():
    file = open("/workspaces/school/google classroom/HighScore.txt", 'r')
    for i in range(10):
        PlayerArray[i][0] = file.readline()
        PlayerArray[i][1] = file.readline()
    file.close

#question 1(c)
def OutputHighScores():
    for i in range(10):
        print(PlayerArray[i][0].rstrip(), PlayerArray[i][1].rstrip())


#question 1(e)(ii)
#question 1(e)(ii)
def Top10List(name,score):
    for i in range(10):
        if score > int(PlayerArray[i][1]):
                for i in range(9,i,-1):
                    tempName = PlayerArray[i][0]
                    tempScore = PlayerArray[i][1]
                    PlayerArray[i][0] = name
                    PlayerArray[i][1] = str(score)
                    
                

#MAIN PROGRAM: question 1(d),(e)(i)
ReadHighScores()
OutputHighScores()

name = str(input("Please input a 3-character player name:"))
while len(name) != 3:
    name = str(input("Please input a valid player name:"))
score = int(input("Please input an integer score between 1 and 100000 inclusive:"))
while score > 100000 or score < 1:
    score = int(input("Please input a valid score:"))


Top10List(name,score)


