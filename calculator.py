from math import factorial as math_factorial
from decimal import *

WRONG_OPERAND_TEXT = 'Wrong operand'


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
        return float(x * y)
    except InvalidOperation:
        return WRONG_OPERAND_TEXT


def divide(x, y):
    try:
        x = Decimal(str(x))
        y = Decimal(str(y))
        return x / y
    except DivisionByZero:
        return "Division by zero error!"
    except InvalidOperation:
        return WRONG_OPERAND_TEXT


def factorial(x):
    try:
        x = Decimal(str(x))
        if x % 1 != 0:
            raise ValueError
        return math_factorial(x)
    except (InvalidOperation, ValueError):
        return WRONG_OPERAND_TEXT