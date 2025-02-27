def factorial(n):
    if n == 1:
        return 1
    else:
       return n*factorial(n-1)

myArray = []

def sumArray():
    sum = 0
    if len(myArray) == 0:
        return sum
    else:
        sum = sum + myArray[]
        return sum

print(sumArray())

# reversing a string

def reverseStr(myString):
   if len(myString) == 1:
       return myString
   else: 
       newString = myString[len(myString)] + reverseStr(myString)
       return newString
   
print(reverseStr("tracy"))