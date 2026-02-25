class Employee:

    """employee class"""

    count_employees = 0
    emloyees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emloyees.append(self) 
        Employee.count_employees += 1

    def fire_employee(self):
        Employee.count_employees -= 1
        Employee.emloyees.remove(self)
    
    @classmethod
    def display_total_employees(cls):
        print(f"There are {cls.count_employees} employees in our company")
    
    @classmethod
    def employees_info(cls):
        for e in cls.emloyees:
            print(f"Name: {e.name}, salary: {e.salary}")

    @classmethod
    def class_info(cls):
        print(f"base: {cls.__base__}")
        print(f"dict: {cls.__dict__}")
        print(f"name: {cls.__name__}")
        print(f"module: {cls.__module__}")
        print(f"doc: {cls.__doc__}")

empl1 = Employee("Viktor", 1000)
empl2 = Employee("Olena", 1500)
Employee.employees_info()

Employee.display_total_employees()
empl3 = Employee("Oleksandr", 2000)
Employee.display_total_employees()

empl2.fire_employee()

Employee.display_total_employees()

Employee.employees_info()

Employee.class_info()

