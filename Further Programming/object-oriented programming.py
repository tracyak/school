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
    def __init__(self,name,age,gender):
        self.name = name # of type string
        self.age = age # of type integer
        self.gender = gender # of type string of single char
    def Walk(self):
        return f"{self.name} is walking."
    def Run(self):
        return f"{self.name} is running."
    def Walk(self):
        return f"{self.name} is talking."
    def PrintPerson(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

person1 = Person("Tracy", 17, "F")
print(person1.name, person1.age, person1.gender)
print(person1.Walk())
print(person1.PrintPerson())
# print(person1.__dict__) # only in python