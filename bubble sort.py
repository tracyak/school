myArray = [12,6,4,27,50,26,18,17,21,13,31,46]

swap = True
Pass = len(myArray) - 1
n = len(myArray)


   
while swap != False:
    swap = False
    for i in range(n-1):
        if myArray[i] > myArray[i+1]:
            Temp = myArray[i]
            myArray[i] = myArray[i+1]
            myArray[i+1] = Temp
            swap = True
    print(myArray)

