class Employee:
    def __init__(self, salary, age) -> None:
        self.salary = salary
        self.age = age

e1 = Employee(2000, 18)
e1_salary = e1.salary
print(e1.__dict__)