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

    def test3(self):
        for x in range(1, 101):
            if x%5 == 0 and x%3 != 0:
                self.assertEqual(FizzBuzz.FizzBuzz(x),"Buzz")
    
    def test4(self):
        for x in range(1, 101):
            if x%5 == 0 and x%3 == 0:
                self.assertEqual(FizzBuzz.FizzBuzz(x),"FizzBuzz")

if __name__ == "__main__":
    unittest.main()

