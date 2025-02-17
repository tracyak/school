
my2DArray = [[12,6,2,27],[26,18,7,21],[12,31,46,50]]


num = int(input("Type the integer you are searching for:"))
rowNum = int(input("Type in which row you would like to search:"))
found = False


for j in range (len(my2DArray[0])):                
    if num == my2DArray[rowNum][j]:
        print("Element found, row", rowNum ,"column", j)
        found = True

if found == False:
    print("Element not found")

print(j)