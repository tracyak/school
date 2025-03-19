# #question 1(a)
# StackData = [] # global integer, 10 elements
# StackPointer = 0 # global integer

# #question 1(b)
# def OutputValues():
#     global StackPointer
#     for i in range(len(StackData)):
#         print(StackData[i])
#     print(StackPointer)

# #question 1(c)
# def Push(num):
#     global StackPointer
#     if len(StackData) == 10:
#         return False
#     else:
#         StackData.append(num)
#         StackPointer += 1
#         if StackPointer == 10:
#             StackPointer = -1
#         return True
    

# #question 1(e)(i)
# def Pop():
#     global StackPointer
#     if len(StackData) == 0:
#         return -1
#     else:
#         tempPointer = StackPointer - 1
#         if tempPointer == -2:
#            tempData = StackData[9]
#            StackData[9] = None
#            StackPointer = 9
#         else:
#             tempData = StackData[tempPointer]
#             StackData[tempPointer] = None
#             StackPointer = tempPointer
#         return tempData

    
# #MAIN PROGRAM, question 1(d)(i)(ii), (e)(ii)
# for i in range(11):
#     num = int(input("Enter an integer to add to the stack:"))
#     if Push(num) == True:
#         print("Number was successfully added to the stack!")
#     else:
#         print("Stack is full, number was not successfully added to the stack.")
# OutputValues()

# print(Pop())
# print(Pop())

# OutputValues()

# import random
# #question 2(a)
# ArrayData = [[random.randint(1,100) for _ in range(10)] for _ in range(10)] #global integer, 10 by 10 elements

# #question 2(b)(ii)
# def OutputValues():
#     for i in range(10):
#         print(ArrayData[i])

# OutputValues()


# #question 2(c)(i)
# def BinarySearch(SearchArray,Lower,Upper,SearchValue):
#     if Upper >= Lower:
#         Mid = (Lower + (Upper - 1)) % 2
#         if SearchArray[0][Mid] == SearchValue:
#             return Mid
#         elif SearchArray[0][Mid] > SearchValue:
#             return BinarySearch(SearchArray,Lower,Mid-1,SearchValue)
#         elif SearchArray[0][Mid] > SearchValue:
#             return BinarySearch(SearchArray,Mid+1,Upper,SearchValue)
#         return -1
    

# #MAIN PROGRAM question 2(b)(i)(iii)
# ArrayLength = 10
# for x in range(ArrayLength):
#     for y in range(ArrayLength-1):
#         for z in range(ArrayLength-y-1):
#             if ArrayData[x][z] > ArrayData[x][z+1]:
#                 TempValue = ArrayData[x][z]
#                 ArrayData[x][z] = ArrayData[x][z+1]
#                 ArrayData[x][z+1] = TempValue

# OutputValues()
# print(ArrayData[0])
# value1 = int(input("Enter a number in the first line of the array:"))
# value2 = int(input("Enter a number that is not in the first line of the arrary:"))
# print(BinarySearch(ArrayData,0,10,value1))
# print(BinarySearch(ArrayData,0,10,value2))

#question 3(a),(b)
class Card:
    def __init__(self,CNum, CColour):
        self.__CNum  = CNum
        self.__CColour = CColour
    
    def GetNumber(self):
        return self.__CNum
    
    def GetColour(self):
        return self.__CColour
    
#question 3(d)
chosenArray = []
def ChooseCard(index):
    if index >= 1 and index <= 30:
        for i in range(len(chosenArray)):
            if cardsArray[index] != chosenArray[i]:
                chosenArray.append(cardsArray[index])
                return index
    else:
        index = int(input("Please enter a valid index between 1 and 30 inclusive:"))
        ChooseCard(index)
        

    
#MAIN PROGRAM, question 3(c)
cardsArray = [None for _ in range(30)]

try: 
    file = open("/workspaces/school/google classroom/9618_s22_qp_42 files/CardValues.txt", 'r')
    for i in range(30):
        num = file.readline()
        colour = file.readline()
        cardsArray[i] = Card(num,colour)
except FileNotFoundError:
    print("Sorry, file does not exist!")

    


    

