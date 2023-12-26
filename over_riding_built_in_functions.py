class Cart:
    def __init__(self, basket1, basket2, basket3) -> None:
        self.clothes = basket1
        self.electronics = basket2
        self.other = basket3
        
    def __len__(self):
        print("total number of items in cart: ")
        return len(self.clothes)+len(self.electronics)+len(self.other)
    
C1 = Cart(["pent", "shirt", "t-shirt"], ["earphone", "mobile"], ['chair'])
# print(C1.__dict__)
print(len(C1))