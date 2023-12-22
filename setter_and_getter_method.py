class Employee:
    def set_name(self, name):
        # Set the name attribute of the instance
        self.name = name

    def get_name(self):
        # Print the name attribute of the instance
        print("The name is:", self.name)

# Instantiate an Employee object
s1 = Employee()

# Call the set_name method to set the name attribute
s1.set_name("XY")

# Call the get_name method to print the name attribute
get_name_data = s1.get_name()

# Print the result of get_name_data (which is None, as get_name does not return anything)
print(get_name_data)
