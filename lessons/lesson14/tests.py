import unittest
from .QuadraticEquation import QuadraticEquation

class TestQuadraticEquation(unittest.TestCase):
    # def test_two_real_roots(self):
    #     eq = QuadraticEquation(1, -5, 6)
    #     self.assertEqual(eq.get_discriminant(), 1)
    #     self.assertEqual(eq.solve(), (3.0, 2.0))

    def test_one_real_root(self):
        eq = QuadraticEquation(1, -2, 1)
        self.assertEqual(eq.get_discriminant(), 0)
        self.assertEqual(eq.solve(), (1.0,))

    def test_no_real_roots(self):
        eq = QuadraticEquation(1, 0, 1)
        self.assertEqual(eq.get_discriminant(), -4)
        self.assertEqual(eq.solve(), "Коренів серед реальних чисел немає (D < 0)")

    def test_linear_equation(self):
        eq = QuadraticEquation(0, 2, -4)
        self.assertEqual(eq.solve(), "Це лінійне рівняння. Корінь: 2.0")

    # def test_no_solution(self):
    #     eq = QuadraticEquation(0, 0, 5)
    #     self.assertEqual(eq.solve(), "Рівняння не має сенсу (0 = 0 або 0 = c)")


if __name__ == '__main__':
    unittest.main()