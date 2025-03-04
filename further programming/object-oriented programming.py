class Car:
    def __init__(self,colour,make,model):  
        self.colour = colour
        self.make = make
        self.model = model
    def start(self):
        print(f"The {self} has started.")
    def stop(self):
        print(f"The {self} has stopped.")

car1 = Car()

print(car1)
print(car1.colour)
print(car1.start())