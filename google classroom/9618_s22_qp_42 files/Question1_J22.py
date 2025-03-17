#question 1(a)
StackData = [] # global integer, 10 elements
StackPointer = 0 # global integer

#question 1(b)
def OutputValues():
    global StackPointer
    for i in range(len(StackData)):
        print(StackData[i])
    print(StackPointer)

#question 1(c)
def Push(num):
    global StackPointer
    if len(StackData) == 10:
        return False
    else:
        StackData.append(num)
        if len(StackData) == 10:
            StackPointer = -1
        else: 
            StackPointer += 1
        return True
    
#question 1(e)(i)
def Pop():
    if len(StackData) == 0:
        return -1
    else:
        temp = StackData[StackPointer]
        StackData[StackPointer] = None
        StackPointer -= 1
        return temp

    
#MAIN PROGRAM, question 1(d)(i)(ii), (e)(ii)
for i in range(11):
    num = int(input("Enter an integer to add to the stack:"))
    if Push(num) == True:
        print("Number was successfully added to the stack!")
    else:
        print("Stack is full, number was not successfully added to the stack.")
OutputValues()

Pop()
Pop()
OutputValues()




