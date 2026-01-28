class Person:
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def show_details(self):
        print("Employee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)


class PartTime(Person):
    def show_details(self):
        print("Part-Time Worker Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)


class Consultant(Employee, PartTime):
    def show_details(self):
        print("Consultant Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)


person1 = Person()
person1.name = "Alice"
person1.age = 25

employee1 = Employee()
employee1.name = "Bob"
employee1.age = 30
employee1.employee_id = "EMP101"

parttime1 = PartTime()
parttime1.name = "Charlie"
parttime1.age = 22
parttime1.working_hours = 20.5

consultant1 = Consultant()
consultant1.name = "David"
consultant1.age = 35
consultant1.employee_id = "CONS201"
consultant1.working_hours = 15.0
consultant1.project_name = "AI Project"

print("\n--- Person ---")
person1.show_details()

print("\n--- Employee ---")
employee1.show_details()

print("\n--- PartTime ---")
parttime1.show_details()

print("\n--- Consultant ---")
consultant1.show_details()
