import pickle
class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

student1 = Student("Tracy", 17)
file1 = open("file1.dat", 'wb')
pickle.dump(student1,file1)
print(student1)
file1.close()

file1 = open("file1.dat", 'rb')
student2 = pickle.load(file1)
print(student2)
file1.close()


