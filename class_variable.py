class Student:
    # Class attribute for college name
    college = "GCS"
    def __init__(self, name, age) -> None:
        # Instance attributes for name and age
        self.name = name
        self.age = age

    
    @classmethod
    def get_college_name(cls):
        # Class method to print the college name
        print(f"College name is: ", cls.college)

# Instantiate a Student object 'st1' with name 'Baber' and age 20
st1 = Student("Baber", 20)


# Uncomment the following lines for additional instances and prints
# st2 = Student("Adeel", 21)
# st3 = Student("Sadaqat", 24)
# print(st1.__dict__)
# print(Student.college)
# print(st1.college)

# Uncomment the following line to modify the college attribute for 'st1'
# st1.college = "YOU"
print(st1.__dict__)
# print(Student.college)

# Call the class method to get and print the college name
Student.get_college_name()

# Call the class method on an instance to achieve the same result
print(st1.get_college_name())