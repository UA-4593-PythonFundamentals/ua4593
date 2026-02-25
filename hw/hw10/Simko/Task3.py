class Employee:
      """Common base class for all employees"""
      empCount = 0
      def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee.empCount += 1
      def printCount(self):
            print("Total number of employees %d" % Employee.empCount)

      def displayEmployee(self):
            print (f"Name: {self.name}, Salary: {self.salary}")


      @classmethod
      def displayInformation(cls):
            print(f"Base classes: {cls.__bases__}")
            print(f"Namespace: {cls.__dict__}")
            print(f"Class name: {cls.__name__}")
            print(f"Module name: {cls.__module__}")
            print(f"Documentation bar: {cls.__doc__}")

if  __name__ == "__main__":
     Employee.displayInformation()


     emp1 = Employee("Zara", 2000)
     emp2 = Employee("Lara", 5000)
     emp3 = Employee("John", 10000)

     emp1.printCount()
     emp1.displayEmployee()
     emp2.displayEmployee()
     emp3.displayEmployee()
