class Employee:
    # Class variable for bonus shared among all instances of Employee
    bonus = 2000
    
    def display(self):
        # Display method for the Employee class
        print("This is employee class method")

class Manager(Employee):
    # Additional class variable for bonus specific to Manager instances
    bonus1 = 1000
    
    def show(self):
        # Show method for the Manager class
        print("This is manager class method")

# Instantiate an Employee object and a Manager object
e1 = Employee()
m1 = Manager()

# Uncomment the following lines for method calls and bonus access
# e1.display()
m1.display()

# Uncomment the following line to access the bonus variable from Manager class
# print(m1.bonus)
