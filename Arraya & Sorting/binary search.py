myArray = [3,8,10,11,16,17,25,31,47,55,59,64,77,79,82,83,93,97]

low = 0
high = len(myArray)
mid = len(myArray) // 2
found = False

num = int(input("please state the integer you want to search for:"))

while (high-low) != 0 and found == False:
    if num == myArray[mid]:
        found = True
        print("Element found, index", mid)
    else:    
        if num > myArray[mid]:
            low = mid + 1
            mid = (low + high) // 2
        else:
            if num < myArray[mid]:
                high = mid - 1
                mid = (low + high) // 2


if num == myArray[0]:
    print("Element found, index 0")
else:
    if found == False:
        print("Element not found")
        
#recursive binary search








                