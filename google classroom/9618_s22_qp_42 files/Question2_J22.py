#question 2(a)

import random

ArrayData = [[random.randint(1,100) for _ in range(10)] for _ in range(10)] #global integer, 10 by 10 elements

#question 2(b)(ii)
def OutputValues():
    for i in range(10):
        print(ArrayData[i])

OutputValues()


#question 2(c)(i)
def BinarySearch(SearchArray,Lower,Upper,SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) % 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray,Lower,Mid-1,SearchValue)
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray,Mid+1,Upper,SearchValue)
        return -1
    

#MAIN PROGRAM question 2(b)(i)(iii)
ArrayLength = 10
for x in range(ArrayLength):
    for y in range(ArrayLength-1):
        for z in range(ArrayLength-y-1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue

OutputValues()
print(ArrayData[0])
value1 = int(input("Enter a number in the first line of the array:"))
value2 = int(input("Enter a number that is not in the first line of the arrary:"))
print(BinarySearch(ArrayData,0,10,value1))
print(BinarySearch(ArrayData,0,10,value2))
