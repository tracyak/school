#second element is the key value
# i is index of key element
# j is i -1

myArray = [12,6,4,27,50,26,18,17,21,13,31,46]


for i in range(1,len(myArray)):
    Key = myArray[i]
    j = i - 1
    while Key < myArray[j] and j >= 0:
        Temp = myArray[j]
        myArray[j] = myArray[j+1]
        myArray[j+1] = Temp
        j = j - 1


print(myArray)
