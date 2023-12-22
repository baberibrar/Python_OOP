# Define a Employee class for maintaining employee data.
class Employee:
    """This is employee class for maintaining employee data"""
    
    # Constructor method to initialize name, salary, age attributes
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age

    # Method to disply employee information
    def display(self):
        print(f"name is {self.name} and age is {self.age}")

# Instantiate an Employee object with name "x", salary 1800, age 18.
e1 = Employee("x", 1800, 18)

# print the docstring of the Employee class.
print(Employee.__doc__)

# print the dictionary containing the class's namespace.
print(Employee.__dict__)

# print the name of Employee class.
print(Employee.__name__)

# print the name of module in which employee class is defined.
print(Employee.__module__)