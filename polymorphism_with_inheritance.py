class Vehicle:
    def __init__(self, name, colour, price) -> None:
        self.name = name
        self.colour = colour
        self.price = price
        
    def get_details(self):
        print("name is: ", self.name)
        print("coloue is: ", self.colour)
        print("price is: ", self.price)
        
    def max_speed(self):
        print("max speed limit is 100")
        
    def gear(self):
        print("max gear is 6")
        
# v1 = Vehicle("Truck", "Red", 10000)
# print(v1.__dict__)

class Car(Vehicle):
    def max_speed(self):
        print("max speed limit is 140")
        
    def gear(self):
        print("gear change is 7")
        

V1 = Vehicle("Truck", "Red", 10000)
C1 = Car("Car", "Blue", 8000)
# print(V1.__dict__)
# print(C1.__dict__)

print(V1.max_speed())
print(C1.max_speed())