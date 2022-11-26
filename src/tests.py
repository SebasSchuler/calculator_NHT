import unittest
import sys

sys.path.append('')
from controller.calculator import Calculator


class TestOperators(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(4, 3)
        self.assertEqual(7, result)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(4, 3)
        self.assertEqual(1, result)

    def test_multiplication(self):
        calculator = Calculator()
        result = calculator.multiplication(4, 3)
        self.assertEqual(12, result)

    def test_division(self):
        calculator = Calculator()
        result = calculator.division(4, 2)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
