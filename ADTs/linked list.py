#linked list

#initializing the Pointer array
linkedlistData = [None for _ in range(10)]
linkedlistPointer = [(_+1) for _ in range(10)]
linkedlistPointer[9] = -1
startPointer = -1
heapPointer = 0


# linkedlistData = [5,6,7,9,None,None,None]
# linkedlistPointer = [-1,0,1,2,5,6,-1] 
# startPointer = 3
# heapPointer = 4

def isFull():
    global heapPointer
    if heapPointer == -1:
        return True
    
def isEmpty():
    global startPointer
    if startPointer == -1:
        return True

def SearchLinkedList(myElement):
    global startPointer
    itemPointer = startPointer
    Found = False
    while itemPointer != -1 and Found != True:
        if myElement == linkedlistData[itemPointer]:
            Found = True
        else:
            itemPointer = linkedlistPointer[itemPointer]
    return itemPointer 

# print(SearchLinkedList(5))
# print(SearchLinkedList(9))
# print(SearchLinkedList(13))

def AddLinkedList(myElement):
    global startPointer
    global heapPointer
    if isFull() != True:
        tempPointer = startPointer
        linkedlistData[heapPointer] = myElement
        startPointer = heapPointer
        if isFull() == True:
            heapPointer = -1
        else:
            heapPointer = linkedlistPointer[startPointer]
        linkedlistPointer[startPointer] = tempPointer
    else:
        print("Linked list is full")

def RemoveLinkedList(myElement):
    global startPointer
    global heapPointer
    itemPointer = startPointer
    tempPointer = itemPointer
    Found = False
    if isEmpty != True:
        while itemPointer != -1 and Found != True:
            if myElement == linkedlistData[itemPointer]:
                Found = True 
            else:
                tempPointer = itemPointer
                itemPointer = linkedlistPointer[itemPointer]
        if itemPointer != -1:
            if startPointer == heapPointer:
                startPointer = linkedlistPointer[tempPointer]
            linkedlistPointer[tempPointer] = linkedlistPointer[itemPointer]
            linkedlistPointer[itemPointer] = heapPointer
            heapPointer = itemPointer
            linkedlistPointer[heapPointer] = linkedlistPointer[itemPointer]
            linkedlistData[itemPointer] = None
        else: 
            print("Element is not found in the linked list")
    else: 
        print("Linked list is empty")

            

    
           

# AddLinkedList(20)
# AddLinkedList(10)
# AddLinkedList(30)
# AddLinkedList(40)

# print(linkedlistData)
# print(linkedlistPointer)
# print(startPointer)
# print(heapPointer)


# RemoveLinkedList(10)
# print(linkedlistData)
# print(linkedlistPointer)
# print(startPointer)
# print(heapPointer)

#DONE FINALLYYYYYYYYYYYYYYYYYYY








