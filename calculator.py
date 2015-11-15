from math import factorial as math_factorial
from decimal import *

WRONG_OPERAND_TEXT = 'Wrong operand'
DIVISION_BY_ZERO_TEXT = 'Division by zero'


def add(x, y):
    try:
        x = Decimal(str(x))
        y = Decimal(str(y))
        return float(x + y)
    except InvalidOperation:
        return WRONG_OPERAND_TEXT


def subtract(x, y):
    try:
        x = Decimal(str(x))
        y = Decimal(str(y))
        return float(x - y)
    except InvalidOperation:
        return WRONG_OPERAND_TEXT


def multiply(x, y):
    try:
        x = Decimal(str(x))
        y = Decimal(str(y))
        return round(x * y, 6)
    except InvalidOperation:
        return WRONG_OPERAND_TEXT


def divide(x, y):
    try:
        x = Decimal(str(x))
        y = Decimal(str(y))
        return round(x / y, 6)
    except DivisionByZero:
        return DIVISION_BY_ZERO_TEXT
    except InvalidOperation:
        if x == 0 and y == 0:
            return DIVISION_BY_ZERO_TEXT
        return WRONG_OPERAND_TEXT


def factorial(x):
    try:
        x = Decimal(str(x))
        if x % 1 != 0 or x < 0:
            raise ValueError
        return math_factorial(x)
    except (InvalidOperation, ValueError):
        return WRONG_OPERAND_TEXT