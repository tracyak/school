# class Car:
#     def __init__(self,colour,make,model):  
#         self.colour = colour
#         self.make = make
#         self.model = model
#     def start(self):
#         print(f"The {self} has started.")
#     def stop(self):
#         print(f"The {self} has stopped.")

# car1 = Car()

# print(car1)
# print(car1.colour)
# car1.start()

class Person:
    personCount = 0
    def __init__(self,name,age,gender):
        self.__name = name # of type string
        self.__age = age # of type integer
        self.__gender = gender # of type string of single char
        Person.personCount += 1

    def walk(self):
        return f"{self.name} is walking."
    
    def run(self):
        return f"{self.name} is running."
    
    def talk(self):
        return f"{self.name} is talking."
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getGender(self):
        return self.__gender
    
    def setName(self,name):
        self.__name = name
    
    def setAge(self,age):
        self.__age = age
    
    def setGender(self,gender):
        self.__gender = gender

    def PrintPerson(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
class Teacher(Person):
    def __init__(self, name, age, gender,salary):
        super().__init__(name, age, gender) #super().__init__(attribute1,2,3,) is used to show the 'IS A' relationship.
        self.__salary = salary
    
    def PrintPerson(self):
        return f"Name: {Person.getName(self)} Age: {Person.getAge(self)}, Gender: {Person.getGender(self)}, Salary: {self.__salary}"

person1 = Person("Tracy", 17, "F")
person2 = Person("Alex", 19, "M")
person3 = Person("Bob", 18, "M")
# print(person1.PrintPerson())
# print(person2.PrintPerson())
# print(person3.PrintPerson())
# print(person1.__dict__) # only in python

teacher1 = Teacher("John,",29,"M",2000)
print(teacher1.PrintPerson())

