num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

try:
    print("Quotient: ", num1 / num2)
except ZeroDivisionError:
    print("Hey!! You can't divide a number by zero.")

try: 
    file = open("tracy.txt", 'r')
except FileNotFoundError:
    print("The file you are trying to open is not found.")
