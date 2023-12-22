class Bank:
    # Class-level attributes
    bank_name = "BOP"
    rate_of_interest = 12.25
    
    @staticmethod
    def simple_interest(principal, years):
        # Calculate simple interest using the static method
        interest = (principal * years * Bank.rate_of_interest) / 100
        print("The interest amount:", interest)

# Get user input for principal amount and number of years
principal = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))

# Call the static method to calculate and print simple interest
Bank.simple_interest(principal, years)

# Solution with @classmethod
# class Bank:
#     # Class-level attributes
#     bank_name = "BOP"
#     rate_of_interest = 12.25
    
#     @classmethod
#     def simple_interest(cls, prin, n):
#         x = (prin*n*cls.rate_of_interest ) / 100
#         print(x)
        
# print(Bank.simple_interest(1000, 5))
