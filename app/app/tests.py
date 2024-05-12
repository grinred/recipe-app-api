from django.test import SimpleTestCase
from app import *


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEquals(res, 11)
