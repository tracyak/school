#google classroom, task 2

#question 1(a)
myArray = [[None for _ in range(2)] for _ in range (11)]

#questoin 1(b)
def ReadHighScores():
    try:
        file = open("HighScore.txt", 'r')
    except FileNotFoundError:
        print("Sorry, the file you tried to open was not found.")
    for i in range(len(file)):
        line = file.readline()
        if i%2 == 0:
            myArray[i][0] = line
        else:
            myArray[i][1] = line

ReadHighScores() 
print(myArray)
