"""
sample tests
"""

from django.test import SimpleTestCase
from app import calcy

class CalcTest(SimpleTestCase):
    def test_add_nums(self):
        res = calcy.add(5,6)
        self.assertEquals(res, 11)

    def test_subtraction(self):
        res= calcy.subtract(10,15)
        self.assertEquals(res, 5)