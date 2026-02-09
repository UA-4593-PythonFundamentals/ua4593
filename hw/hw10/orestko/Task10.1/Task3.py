class Employee:
   
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

   
    def info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

   
    @classmethod
    def total_employees(cls):
        return f"Total employees: {cls.employee_count}"
    

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)


print(emp1.info())
print(emp2.info()) 

print("Base classes:", Employee.__base__)
print("Namespace (__dict__):", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation (__doc__):", Employee.__doc__)