class Employee:
    """Клас для представлення співробітників компанії."""
    
    # Змінна класу для лічильника
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def display_total_count(cls):
        print(f"Кількість співробітників: {cls.employee_count}")

# 1. Створення об'єктів
emp1 = Employee("Іван", 50000)
emp2 = Employee("Марія", 60000)

# 2. Вивід інформації про співробітників
emp1.display_employee()
emp2.display_employee()
Employee.display_total_count()

print("\n--- Інформація про клас ---")

# 3. Вивід атрибутів класу
print(f"Базові класи (__bases__): {Employee.__bases__}")
print(f"Простір імен (__dict__): {Employee.__dict__}")
print(f"Ім'я класу (__name__): {Employee.__name__}")
print(f"Назва модуля (__module__): {Employee.__module__}")
print(f"Документація (__doc__): {Employee.__doc__}")