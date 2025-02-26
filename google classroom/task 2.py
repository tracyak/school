#google classroom, task 2

#question 1(a)
NameArray = [] #global string, 11 elements
ScoreArray = [] #global integer, 11 elements

#questoin 1(b)
def ReadHighScores():
    file = open("/workspaces/school/google classroom/HighScore.txt", 'r')
    i = 0
    for line in file:
        if i%2 == 0:
            NameArray.append(str(line.rstrip()))
        else:
            ScoreArray.append(int(line.rstrip()))
        i +=1


ReadHighScores() 
print(NameArray)
print(ScoreArray)

