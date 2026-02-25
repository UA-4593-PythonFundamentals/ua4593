class Employee:
    employee_count = 0
    employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.employee_count += 1
        Employee.employees.append(self)

    @classmethod
    def get_employee_number(cls):
        print(f'Total number of employees: {cls.employee_count}')

    def get_employee_info(self):
        print(f'Employee {self.name} has a salary of {self.salary} $')

    @classmethod
    def list_of_employees(cls):
        print('Employees:')
        for emp in cls.employees:
            print(f'Name: {emp.name}, Salary: {emp.salary}')

    @classmethod
    def class_info(cls):
        print(f'1. Class name: {cls.__name__}')
        print(f'2. Base classes: {cls.__base__}')
        print(f'3. Module name: {cls.__module__}')
        print(f'4. Class namespace: {cls.__dict__}')
        print(f'5. Documentation: {cls.__doc__}')
        

john = Employee('John', 1200)
jane = Employee('Jane', 1100)
joe = Employee('Joe', 1000)

Employee.class_info()
print('----------------------------------------------------------------------')

Employee.get_employee_number()
print('----------------------------------------------------------------------')

john.get_employee_info()
jane.get_employee_info()
joe.get_employee_info()
print('----------------------------------------------------------------------')

Employee.list_of_employees()
print('----------------------------------------------------------------------')