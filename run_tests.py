# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test_calculator import AddTestCase, SubtractTestCase, MultiplyTestCase, DivideTestCase, FactorialTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AddTestCase),
        unittest.makeSuite(SubtractTestCase),
        unittest.makeSuite(MultiplyTestCase),
        unittest.makeSuite(DivideTestCase),
        unittest.makeSuite(FactorialTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
