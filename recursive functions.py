def factorial(n):
    if n == 1:
        return 1
    else:
       return n*factorial(n-1)

myArray = [1,2,3,4,5,6,7,8,9,10]

def sumArray():
    sum = 0
    if len(myArray) == 0:
        return 0
    else:
        return sum + sumArray()

print(sumArray())
#reversing a string

# def reverseStr(myString):
#     n = len(myString):
    