# question 1(a), declaring 2D array and variable
Jobs = [[]]#  global integer, 100 by 2 elements
NumberOfJobs = 0  # global integer

#question 1(b)
def Initialise():
    global Jobs
    global NumberOfJobs
    Jobs = [[-1 for _ in range(2)]for _ in range(100)]
    NumberOfJobs = 0

#question 1(c)
def AddJob(jobNum,prio):
    global Jobs 
    global NumberOfJobs
    if NumberOfJobs != 100:
        Jobs[NumberOfJobs] = [jobNum,prio]
        NumberOfJobs += 1
        print("Added")
    else:
        print("Not added")

def InsertionSort():
    global Jobs
    global NumberOfJobs
    for i in range(1,NumberOfJobs):
        Key = Jobs[i][1]
        j = i - 1
        while Key < Jobs[j][1] and j >= 0:
            Temp = Jobs[j]
            Jobs[j] = Jobs[j+1]
            Jobs[j+1] = Temp
            j = j - 1

def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        print(Jobs[i][0], "priority", Jobs[i][1])

#main program, 1(d) and 1(g)
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
InsertionSort()
PrintArray()