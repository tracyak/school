def factorial(n):
    if n == 1:
        return 1
    else:
       return n*factorial(n-1)
    
# print(factorial(5))

myArray = [1,2,3,4,5,6,7,8,9,10]

def sumArray(myArray):
    n = len(myArray)
    if n == 1:
        return myArray[0]
    else:
        return myArray[0] + sumArray(myArray[1:n])

# print(sumArray(myArray))

# reversing a string

def reverseStr(myString):
   n = len(myString)
   if n == 1:
        return myString[-1]
   else: 
        return myString[-1] + reverseStr(myString[:-1])
   
# print(reverseStr("tracy"))

def letterCount(myString,letter):
    n = len(myString)
    if letter != myString[n-1]:
        return 0
    else:
        return 1 + letterCount(myString[:-1],letter)
    
print(letterCount("aaa","a"))
print(letterCount("tracy","y"))

