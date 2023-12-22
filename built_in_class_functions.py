# Define a simple Employee class with attributes name, salary, and age.
class Employee:
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age

# Instantiate an Employee object with the name "xyz", salary 2000, and age 18.
e1 = Employee("xyz", 2000, 18)

# Uncomment the following lines to demonstrate additional operations:

# Get the salary attribute of e1 using getattr.
# get_e1_salary = getattr(e1, "salary")

# Set the age attribute of e1 to 20 using setattr.
# set_e1_age = setattr(e1, "age", 20)

# Delete the age attribute of e1 using delattr.
# del_e1_age = delattr(e1, "age")

# Check if e1 has the salary attribute using hasattr.
# has_e1_salary = hasattr(e1, "salary")

# Print the name attribute of e1.
print(e1.name)
