class User:
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        return 2025 - self.joining_year



class Customer(User):
    
    def show_info(self):
        years = self.years_on_platform()
        print(f"\n{self.name} is a Customer and has used the platform for {years} years")


class Vendor(User):
    
    def show_info(self):
        years = self.years_on_platform()
        print(f"{self.name} is a Vendor and has used the platform for {years} years\n")
    

customer1 = Customer('Alice', 2020)
vendor1 = Vendor('rahul', 2022)

customer1.show_info()
vendor1.show_info()