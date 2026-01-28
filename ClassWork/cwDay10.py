class User:
    def years_on_platform(self):
        return 2025 - self.joining_year

    def show_info(self):
        print("Name:", self.name)
        print("Role:", self.role())
        print("Years on platform:", self.years_on_platform())
        print()


class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"


customer1 = Customer()
customer1.name = "Alice"
customer1.joining_year = 2020


vendor1 = Vendor()
vendor1.name = "Bob"
vendor1.joining_year = 2018


customer1.show_info()
vendor1.show_info()
   