# class Outer:
#     def __init__(self) -> None:
#         print("outer class constructor called")
    
#     def display(self):
#         print("This is display method")
        
        
#     class Inner:
#         def __init__(self) -> None:
#             print("inner class constructor called")
            
#         def show(self):
#             print("This is show method")
            
# obj = Outer()
# in1 = obj.Inner()
# in1.show()

class Student:
    def __init__(self, name, roll, dd, mm, yy) -> None:
        self.name = name
        self.roll = roll
        self.dob = self.DOB(dd, mm, yy)
    
    def display(self):
        print(f"Name is {self.name} and roll no is {self.roll}")
        self.dob.display()
    
    class DOB:
        def __init__(self, dd, mm, yy) -> None:
            self.date = dd
            self.month = mm
            self.year = yy
            
        def display(self):
            print(f"Date of birth is: {self.date}/{self.month}/{self.year}")

s1 = Student("X", 1122, 10, 12, 2000)
result = s1.display()
print(result)