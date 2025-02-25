#question 1(a)(i)
DataArray = [] #25 data items of type integer

#question 1(a)(ii)
file = open("/workspaces/school/google classroom/Data.txt",'r')
for line in file:
    DataArray.append(int(line.rstrip()))

#question 1(b)(i)
def PrintArray(DataArray):
    for i in range(len(DataArray)):
        print(DataArray[i], end = " ")

#question 1(c)
def LinearSearch(myIntArray,myInt):
    count = 0
    for i in range(len(myIntArray)):
        if myInt == myIntArray[i]:
            count += 1 
    return count

#main program question 1(b)(iI),(iii),(d)(i),(ii)
if __name__ == "__main__":
    PrintArray(DataArray)
    myNum = int(input("Please input a whole number between 0 and 100 inclusive:"))
    while myNum < 0 or myNum > 100:
        myNum = int(input("Please input a a valid number:"))
    print("The number", myNum, "is found", LinearSearch(DataArray,myNum),"times.")



