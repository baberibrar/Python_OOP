class Country:
    def __init__(self, office) -> None:
        print("Country class constructor")
        self.office = office
        
    # def display(self):
    #     print('This is Country method')
    
class State:
    def __init__(self, office) -> None:
        print("State class constructor")
        self.office = office
        
    # def display(self):
    #     print('This is State method')
    
class District(State, Country):
    def __init__(self, office) -> None:
        print("District class constructor")
        super().__init__(office)
        self.office = office
    
        

d = District("LHR")
# print(d.display())
# print(d.__dict__)