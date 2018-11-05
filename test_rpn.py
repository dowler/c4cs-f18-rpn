import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_percent(self):
        result = rpn.calculate("1 100 %")
        self.assertEqual(1, result)
    def test_exponent(self):
        result = rpn.calculate("2 6 ^")
        self.assertEqual(64, result)
    def test_intdivision(self):
        result = rpn.calculate("5 5 //")
        self.assertEqual(1, result)
        result = rpn.calculate("11 3 //")
        self.assertEqual(3, result)
    def test_and(self):
        result = rpn.calculate("1 2 &")
        self.assertEqual(0, result)
    def test_or(self):
        result = rpn.calculate("1 2 |")
        self.assertEqual(3, result)
    def test_not(self):
        result = rpn.calculate("5 2 !")
        self.assertEqual(7, result)
    def test_pi(self):
        result = rpn.calculate("pi pi /")
        self.assertEqual(1, result)
    def test_e(self):
        result = rpn.calculate("e e /")
        self.assertEqual(1, result)
    def test_sin(self):
        result = rpn.calculate("0 sin")
        self.assertEqual(0, result)
    def test_cos(self):
        result = rpn.calculate("0 cos")
        self.assertEqual(1, result)
    
    

if __name__ == '__main__':
    unittest.main()