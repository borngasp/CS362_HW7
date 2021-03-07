import unittest
import FizzBuzz


class FizzBuzzTestCases(unittest.TestCase):

    def test1(self):
        for x in range(1, 101):
            self.assertEqual(type(FizzBuzz.FizzBuzz(x)),str)

if __name__ == "__main__":
    unittest.main()

