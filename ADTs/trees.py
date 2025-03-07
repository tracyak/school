#declaring tree using array
# myTree = [[ -1 for _ in range(3)] for _ in range(10)]
# for i in range(10):
#     myTree[i][1] = i + 1
#     if i == 9:
#         myTree[i][1] = -1
#     print(myTree[i])

# myTree = [[ -1, _+1, -1] if _ != 9 else [-1]*3 for _ in range(10)]
# for i in range(10):
#     print(myTree[i])

# in algorithm to add element to tree, first check if the tree is empty or full.
# store the previous value of dataPtr in tempPtr (this is the value of the next free location)
# # if empty, rootPointer will point to this node and leftPtr and rightPtr stays as -1.
# replace the value of dataPtr to the element to be added. 
# if not empty, check if leftPtr and rightPtr is pointing to any child/subtree (if the pointers are null)
# if there is no child/subtree on the root, set left/rightPtr to tempPtr so as to show that this new node is a child of that existing node
#at the end, set freePtr 

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
    while itemPtr != -1:
            if myElement == myTree[itemPtr][1]:
                return itemPtr
            if myElement < myTree[itemPtr][1]:
                itemPtr = myTree[itemPtr][0]
            if myElement > myTree[itemPtr][1]:
                itemPtr = myTree[itemPtr][2]
    return -1
        

        
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
                


        




