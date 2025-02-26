#Question 1(a)
DataArray = [None for _ in range(100)]

#Question 1(b)
def ReadFile():
    global DataArray
    file = open("/workspaces/school/google classroom/IntegerData.txt", 'r')
    i = 0
    for line in file:
        DataArray[i] = int(line.rstrip())
        i = i + 1

#Question 1(c)
def FindValues():
    global DataArray
    myNum = int(input("Enter a whole number between 1 and 100 inclusive to be searched in the array:"))
    if myNum < 1 and myNum > 100:
        print("Please enter a valid number to be searched.")
    else:
        numCount = 0
        for i in range(len(DataArray)):
            if myNum == DataArray[i]:
                numCount = numCount + 1
        return numCount

#Question 1(d)(i),(ii)
ReadFile()
print("This number appeared", FindValues(),"times in the array.")

#Question 1(e)
def BubbleSort():
    global DataArray
    swap = True
    Pass = len(DataArray) - 1
    n = len(DataArray)
    while swap != False:
        swap = False
        for i in range(len(DataArray)-1):
            if DataArray[i] > DataArray[i+1]:
                Temp = DataArray[i]
                DataArray[i] = DataArray[i+1]
                DataArray[i+1] = Temp
                swap = True
    print(DataArray)

BubbleSort()