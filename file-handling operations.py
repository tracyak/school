file = open("Numbers.txt", 'r')
print(file.read())
print(file.readline())
print(file.readlines())

#output file as list VS as it looks in the file
text = file.readlines() #READLINES() CANNOT BE USED IN THE EXAM,YOU MUST USE ALTERNATIVE METHODS DURING EXAM 
print(text)
for i in range(len(text)):
    print(text[i])

#either create your own array and use readline() only, or use this code below:
#remember that you should not use append while using indexing, only append into an empty array
numberArr = []
for line in file:
    numberArr.append(int(line.rstrip()))
print(numberArr)

#\n must be manually stripped off from the list elements when typecasting using rstrip() method
#lstrip() for leading spaces, rstrip() for ending spaces, strip() for both spaces
#when using a file, DATA CLEANING MUST BE DONE USING STRIP COMMANDS
total = 0 
for i in range(len(text)):
    total = total + int(text[i].rstrip())

#always remember to close the file at the end of its use
file.close()


