class Employee:
    count = 0
    employees = []
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
        Employee.employees.append(self)
    
    @classmethod
    def get_count(cls):
        return cls.count
    @classmethod
    def get_info(cls):
        print(f"Total amount of employees: {Employee.count}")
        print("   Name:  \t   Salary:  ")
        for employee in Employee.employees:
            print(f"| {employee.name} | \t | {employee.salary} |")

    

em1 = Employee("Artur", "3000")
em2 = Employee('David', '6000')
Employee.get_info()