class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def display(self):
        print("This is person display method")
        
        
class Student(Person):
    def __init__(self, name, age, st_id) -> None:
        super().__init__(name, age)
        self.st_id = st_id
        
    def display(self):
        print("This is Student display method")
        
        

class Employee(Person):
    def __init__(self, name, age, emp_id) -> None:
        super().__init__(name, age)
        self.emp_id = emp_id
        
    def display(self):
        print("This is Employee display method")

employee_obj = Employee("X", 20, 1122)
# print(employee_obj.__dict__)
print(employee_obj.display())