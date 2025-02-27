def factorial(n):
    if n == 1:
        return 1
    else:
       return n*factorial(n-1)

myArray = [1,2,3,4,5,6,7,8,9,10]

def sumArray(myArray):
    n = len(myArray)
    if n == 1:
        return myArray[0]
    else:
        return myArray[0] + sumArray(myArray[1:n])

print(sumArray(myArray))

# reversing a string

def reverseStr(myString):
   n = len(myString)
   newString = myString[n-1]
   if n == 1:
        return myString
   else: 
        return reverseStr(myString[n-1:1]) + newString
   
print(reverseStr("tracy"))