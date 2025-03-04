
stackArr = [None for _ in range(5)]

basePointer = 0
topPointer = -1
stackFull = 4

def isFull():
    global topPointer
    global stackFull
    if topPointer == stackFull:
        return True
    
def isEmpty():
    global topPointer
    if topPointer < 0:
        return True

def Pop():
    global topPointer
    if isEmpty() != True:
        temp = stackArr[topPointer]
        stackArr[topPointer] = None
        topPointer = topPointer - 1
        print("Element", temp, "has been popped")
    else:
        print("There are no elements in the stack")

def Push(myElement):
    global topPointer
    if isFull != True:
        topPointer = topPointer + 1
        stackArr[topPointer] = myElement
        print(myElement, "has been pushed")
    else:
        print("Stack is full, no more elements can be pushed")


