import Calc
import unittest

class TestCalculator(unittest.TestCase):
    def test_Add(self):
        x = 5
        y = 10
        result = Calc.Add(x,y)
        self.assertEqual(result, x+y)

    def test_Sub(self):
        x = 5
        y = 10
        result = Calc.Sub(x,y)
        self.assertEqual(result, x-y)

    def test_Mul(self):
        x = 5
        y = 10
        result = Calc.Mul(x,y)
        self.assertEqual(result, x*y)

    def test_Div(self):
        x = 5
        y = 10
        result = Calc.Div(x,y)
        self.assertEqual(result, x/y)





if __name__ == "__main__":
    unittest.main()
