import unittest
import FizzBuzz


class FizzBuzzTestCases(unittest.TestCase):

    def test1(self):
        for x in range(1, 101):
            self.assertEqual(type(FizzBuzz.FizzBuzz(x)),str)
    
    def test2(self):
        for x in range(1, 101):
            if x%3 == 0 and x%5 != 0:
                self.assertEqual(FizzBuzz.FizzBuzz(x),"Fizz")

if __name__ == "__main__":
    unittest.main()

