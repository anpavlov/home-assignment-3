# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from calculator import *
import unittest


class AddTestCase(unittest.TestCase):
    def test_add_int_int(self):
        self.assertEqual(add(51, 97), 148)

    def test_add_int_float(self):
        self.assertEqual(add(9, -5.67), 3.33)

    def test_add_int_zero(self):
        self.assertEqual(add(257, 0), 257)

    def test_add_float_float(self):
        self.assertEqual(add(0.2, 0.1), 0.3)

    def test_add_float_zero(self):
        self.assertEqual(add(9.521, 0), 9.521)
        
    def test_add_result_zero(self):
        self.assertEqual(add(42.123, -42.123), 0)

    def test_add_zero_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_wrong_operand(self):
        self.assertEqual(add('$%^&*', 8), WRONG_OPERAND_TEXT)

    def test_add_wrong_operand_both(self):
        self.assertEqual(add('minus one', 'twelve'), WRONG_OPERAND_TEXT)


class SubtractTestCase(unittest.TestCase):
    def test_subtract_int_int(self):
        self.assertEqual(subtract(51, 97), -46)

    def test_subtract_int_float(self):
        self.assertEqual(subtract(9, -5.67), 14.67)

    def test_subtract_int_zero(self):
        self.assertEqual(subtract(257, 0), 257)

    def test_subtract_float_float(self):
        self.assertEqual(subtract(0.1, 0.2), -0.1)

    def test_subtract_zero_float(self):
        self.assertEqual(subtract(0, 9.521), -9.521)

    def test_subtract_zero_zero(self):
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_result_zero(self):
        self.assertEqual(subtract(42.123, 42.123), 0)

    def test_subtract_wrong_operand(self):
        self.assertEqual(subtract('(&^%$', 7), WRONG_OPERAND_TEXT)

    def test_subtract_wrong_operand_both(self):
        self.assertEqual(subtract('minus one', 'twelve'), WRONG_OPERAND_TEXT)


class MultiplyTestCase(unittest.TestCase):
    def test_multiply_int_int(self):
        self.assertEqual(multiply(51, 97), 4947)

    def test_multiply_int_float(self):
        self.assertEqual(multiply(9, -5.67), -51.03)

    def test_multiply_int_zero(self):
        self.assertEqual(multiply(257, 0), 0)

    def test_multiply_float_float(self):
        self.assertEqual(multiply(58.324, 12.95), 755.2958)

    def test_multiply_float_zero(self):
        self.assertEqual(multiply(9.521, 0), 0)

    def test_multiply_zero_zero(self):
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_wrong_operand(self):
        self.assertEqual(multiply('@#$%', 0), WRONG_OPERAND_TEXT)

    def test_multiply_wrong_operand_both(self):
        self.assertEqual(multiply('minus one', 'twelve'), WRONG_OPERAND_TEXT)


class DivideTestCase(unittest.TestCase):
    def test_divide_int_int(self):
        self.assertEqual(divide(51, 97), 0.525773)

    def test_divide_int_float(self):
        self.assertEqual(divide(9, -5.67), -1.587302)

    def test_divide_float_float(self):
        self.assertEqual(divide(58.324, 12.95), 4.503784)

    def test_divide_by_zero(self):
        self.assertEqual(divide(9.521, 0), DIVISION_BY_ZERO_TEXT)

    def test_divide_zero_by_zero(self):
        self.assertEqual(divide(0, 0), DIVISION_BY_ZERO_TEXT)

    def test_divide_wrong_operand(self):
        self.assertEqual(divide('@#$%', 8), WRONG_OPERAND_TEXT)

    def test_divide_wrong_operand_both(self):
        self.assertEqual(divide('minus one', 'twelve'), WRONG_OPERAND_TEXT)


class FactorialTestCase(unittest.TestCase):
    def test_factorial_int(self):
        self.assertEqual(factorial(9), 362880)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_float(self):
        self.assertEqual(factorial(4.51), WRONG_OPERAND_TEXT)

    def test_factorial_negative_int(self):
        self.assertEqual(factorial(-257), WRONG_OPERAND_TEXT)

    def test_factorial_wrong_operand(self):
        self.assertEqual(factorial('@#$%'), WRONG_OPERAND_TEXT)