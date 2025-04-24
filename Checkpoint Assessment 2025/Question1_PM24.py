class Employee:
    def __init__(self,Name,EmployeeID,Department):
        self._Name = Name #of type string
        self.__EmployeeID = EmployeeID #of type integer
        self.__Department = Department #of type string
    
    def GetName(self):
        return self.__Name
    
    def GetEmployeeID(self):
        return self.__EmployeeID
    
    def GetDepartment(self):
        return self.__Department
    
    def ChangeDepartment(self,NewDepartment):
        self.__Department = NewDepartment

AllEmployees = [] #1D array of 10 instances of Employee
for i in range(10):
    try:
        file = open("Employees.txt", 'r')
        Employee1 = Employee(file.readline(),int(file.readline()),file.readline())
        AllEmployees.append(Employee1)
    except FileNotFoundError:
        print("Error, file not found!")

print(AllEmployees)