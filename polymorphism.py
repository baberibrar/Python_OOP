"""
> Polymorphism in python is an ability of python object to take many forms.
> If a variable, object, method performs different behaviour according to situation is called Polymorphism
"""


"""
1. Method Overloading:
Method overloading in Python is achieved by defining multiple methods in a class with the same name but different parameters.
"""

class BMW:
    def fuel_type(self):
        print("Diesel")
        
    def max_speed(self):
        print("Max speed is 200")
        
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed is 180")
        
        
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()
    
bmw = BMW()
car_details(bmw)

ferrari = Ferrari()
car_details(ferrari)