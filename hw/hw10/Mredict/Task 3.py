class Employee:
    ''' Class to manage employee information and count '''

    counter = 0
    employees = {}

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
        Employee.employees[self.name] = self.salary
        
    def number_of_employees(self):
        return Employee.counter
    
    @classmethod
    def display_all_info(cls):
        return f"Employees: {cls.employees}"
    
    def __del__(self):
        Employee.counter -= 1
        del Employee.employees[self.name]

    @classmethod
    def class_info(cls):
        print (f"\nClass Name: {cls.__name__}")
        print (f"Documentation: {cls.__doc__}")
        print (f"Base Classes: {cls.__bases__}")
        print (f"Module: {cls.__module__}")
        print (f"Attributes and Methods: {list(cls.__dict__.keys())}\n")

# Example usage
if __name__ == "__main__":
    Employee.class_info()

    emp1 = Employee("John", 50000)
    emp2 = Employee("Jane", 60000)
    emp3 = Employee("Doe", 55000)

    print(f"Number of employees: {emp1.number_of_employees()}")
    print(Employee.display_all_info())

    del emp2

    print(f"Number of employees after deletion: {emp1.number_of_employees()}")
    print(Employee.display_all_info())
