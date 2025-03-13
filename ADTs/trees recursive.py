myTree = [[1,9,2],[3,7,-1],[4,13,5],[-1,5,-1],[-1,12,-1],[-1,15,-1],[-1,7,-1],[-1,8,-1],[-1,9,-1],[-1,-1,-1]]
rootPtr = 0
freePtr = 6

def isEmpty():
    if freePtr == -1 and rootPtr == -1:
        return True
    
def isFull():
    if freePtr == -1:
        return True


def SearchTree(myElement):
    global rootPtr
    global freePtr
    itemPtr = rootPtr
    if itemPtr == -1:
        return -1
    elif myElement == myTree[itemPtr][1]:
        return itemPtr
    elif myElement < myTree[itemPtr][1]:
        itemPtr = SearchTree(myTree[itemPtr][0])
    elif myElement > myTree[itemPtr][1]:
        itemPtr = SearchTree(myTree[itemPtr][2])
 
        
        

        
def InsertTree(myElement):
    global rootPtr
    global freePtr
    if isFull() == True:
        print("The tree is full, element was not added successfully")
    elif isEmpty() == True:
        rootPtr = freePtr
        freePtr = myTree[freePtr][1]
        myTree[rootPtr][1] = myElement
    else:
        newItemPtr  = freePtr
        freePtr = myTree[freePtr][1]
        myTree[newItemPtr][1] = myElement
        itemPtr = rootPtr
        while itemPtr != -1:  
            left = False
            right = False 
            if myElement < myTree[itemPtr][1]:
                left = True
                tempPtr = itemPtr
                itemPtr = myTree[itemPtr][0]
            elif myElement > myTree[itemPtr][1]:
                right = True
                tempPtr = itemPtr
                itemPtr = myTree[itemPtr][2]
        if left == True:
            myTree[tempPtr][0] = newItemPtr
        elif right == True:
            myTree[tempPtr][2] = newItemPtr

if __name__ == "__main__":       
    InsertTree(10)
    for i in range(10):
        print(myTree[i])
    print(rootPtr)
    print(freePtr)
print(SearchTree(10))
                


        




