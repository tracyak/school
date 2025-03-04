myArray = [12,6,2,27,26,18,7,21,12,31]
sum = 0
max = myArray[0]
min = myArray[0]

for i in range(len(myArray)):
    sum = sum + myArray[i-1]
    if myArray[i-1] > max:
        max = myArray[i-1]
    if myArray[i-1] < min:
        min = myArray[i-1]
print(sum)
print(min) 
print(max)