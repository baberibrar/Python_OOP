class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    # instance method
    def display(self):
        print(self.name, self.marks, self.age)

    def change_data(self, marks):
        self.marks = marks


st1 = Student("X", 80)
# outside the class  
st1.age = 20

st2 = Student("Y", 70)

# print(st1.__dict__)
# print(st2.__dict__)

# st1.display()
latest_data_of_st1 = st1.change_data(65)
print(st1.__dict__)
