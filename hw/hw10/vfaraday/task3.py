class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def print_total(cls):
        print(f"Total Employees: {cls.total_employees}")

    def display_info(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")


emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)

emp1.display_info()
Employee.print_total()


print("Class Introspection Results:")
print(f"Base Class (__base__): {Employee.__base__}")

print(f"Namespace (__dict__): {Employee.__dict__}")

print(f"Class Name (__name__): {Employee.__name__}")

print(f"Module Name (__module__): {Employee.__module__}")

print(f"Documentation (__doc__): {Employee.__doc__}")