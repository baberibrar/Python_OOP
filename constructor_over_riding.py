class Father:
    def __init__(self) -> None:
        print("father constructor called")
        self.vehical = "scooter"

class Son(Father):
    def __init__(self) -> None:
        print("son constructor called")
        self.vehical = "BMW"

son_obj = Son()
# print(son_obj.vehical)
print(son_obj.__dict__)
