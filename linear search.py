

import random
myArray = [random.randint(1,100) for _ in range(10)]

print(myArray)


num = int(input("Type the integer you are searching for:"))
found = False

for i in range(len(myArray)):
   if num == myArray[i]:
        found = True
        print("Element is found") 
   
    
if found == False:
    print("Element not found")


     
       