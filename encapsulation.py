class Finance:
    def __init__(self) -> None:
        self.book = 10                  # public data
        self.__revenue = 10000          # private data
        self._number_of_sales = 104     # protected 
    
    def display(self):
        print(f"The revenue value is {self.__revenue}, and book value is {self.book}")
        
f1=Finance()
print(f1._Finance__revenue)     # access private date
print(f1.display())

# class HR:
#     def __init__(self) -> None:
#         self.number_of_emp = 50
#         # rev = f1.revenue = 1
#         # print(rev)
#         print(f1.revenue)

# h1 = HR()
# print(h1.__dict__)