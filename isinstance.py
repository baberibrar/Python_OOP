class Demo:
    pass

d1 = Demo()

class Employee:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(f"Employee name is {self.name}, and age is {self.age}")

e1 = Employee('X', 21)

print(isinstance(e1, Employee))
# output True

print(isinstance(e1, Demo))
# output False