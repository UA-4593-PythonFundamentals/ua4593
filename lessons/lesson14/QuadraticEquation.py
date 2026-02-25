import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminant(self):
        """Обчислює дискримінант: D = b^2 - 4ac"""
        return self.b**2 - 4 * self.a * self.c

    def solve(self):
        """Знаходить корені рівняння"""
        if self.a == 0:
            if self.b == 0:
                return "Рівняння не має сенсу (0 = 0 або 0 = c)"
            return f"Це лінійне рівняння. Корінь: {-self.c / self.b}"

        d = self.get_discriminant()

        if d > 0:
            x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(d)) / (3 * self.a)
            return x1, x2
        elif d == 0:
            x = -self.b / (2 * self.a)
            return x,
        else:
            return "Коренів серед реальних чисел немає (D < 0)"

