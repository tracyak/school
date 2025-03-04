my2DArray = [[12,6,2,27],[26,18,7,21],[12,31,46,50]]

# print(my2DArray)
# print(len(my2DArray))
# print(len(my2DArray[0]))

# print(my2DArray[0][0])

# print(my2DArray[0][1])

# print(my2DArray[0][2])


for i in range(len(my2DArray)):
    sumRow = 0
    for j in range(len(my2DArray[i])):
        sumRow = sumRow + my2DArray[i][j]
    print(sumRow)

for i in range(len(my2DArray[i])):
    sumColumn = 0
    for j in range(len(my2DArray)):
        sumColumn = sumColumn + my2DArray[j][i]
    print(sumColumn)