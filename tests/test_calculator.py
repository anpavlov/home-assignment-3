# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from calculator import *
import unittest


class CalculatorTestCase(unittest.TestCase):
    def test_add_int_int(self):
        self.assertEquals(add(51, 97), 148)

    def test_add_int_negative_int(self):
        self.assertEquals(add(59, -64), -5)

    def test_add_int_float(self):
        self.assertEquals(add(4, 2.5175), 6.5175)

    def test_add_int_negative_float(self):
        self.assertEquals(add(9, -5.67), 3.33)

    def test_add_int_zero(self):
        self.assertEquals(add(257, 0), 257)

    def test_add_negative_int_negative_int(self):
        self.assertEquals(add(51, -97), -46)

    def test_add_negative_int_float(self):
        self.assertEquals(add(-6, 8.65), 2.65)

    def test_add_negative_int_negative_float(self):
        self.assertEquals(add(-78, -17.943), -95.943)

    def test_add_negative_int_zero(self):
        self.assertEquals(add(-8151, 0), -8151)

    def test_add_float_float(self):
        self.assertEquals(add(0.2, 0.1), 0.3)

    def test_add_float_negative_float(self):
        self.assertEquals(add(0.1, -0.3), -0.2)

    def test_add_float_zero(self):
        self.assertEquals(add(9.521, 0), 9.521)

    def test_add_negative_float_negative_float(self):
        self.assertEquals(add(-0.2, -0.1), -0.3)

    def test_add_negative_float_zero(self):
        self.assertEquals(add(-0.223, 0), -0.223)

    def test_add_zero_zero(self):
        self.assertEquals(add(0, 0), 0)

    def test_add_result_zero(self):
        self.assertEquals(add(42.123, -42.123), 0)

    def test_add_wrong_operand(self):
        self.assertEquals(add('some str', 0), WRONG_OPERAND_TEXT)

    def test_add_wrong_operand_both(self):
        self.assertEquals(add('minus one', 'twelve'), WRONG_OPERAND_TEXT)