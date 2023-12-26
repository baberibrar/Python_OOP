class Hotel:
    def __init__(self, name, fare) -> None:
        self.name = name
        self.fare = fare
        
    def __gt__(self, other):
        result = self.fare > other.fare
        return result
    
h1 = Hotel("PC", 25000)
h2 = Hotel("Avari", 2000)

print("Fear: ", h1>h2)