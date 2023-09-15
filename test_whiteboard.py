from unittest import TestCase, main
from whiteboard import fizzbuzz, fizzbuzz2

class TestFizzBuzz(TestCase):

    def test_div_by_15(self):
        result_1 = fizzbuzz(15)
        self.assertEqual(result_1, 'FizzBuzz')
        result_2 = fizzbuzz(30)
        self.assertEqual(result_2, 'FizzBuzz')
        self.assertEqual(fizzbuzz(60), 'FizzBuzz')

    def test_div_by_3(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(9), 'Fizz')
        self.assertEqual(fizzbuzz(12), 'Fizz')
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')

    def test_div_by_5(self):
        self.assertEqual(fizzbuzz(25), 'Buzz')
        self.assertEqual(fizzbuzz(35), 'Buzz')
        self.assertEqual(fizzbuzz(45), 'FizzBuzz')
        self.assertEqual(fizzbuzz(55), 'Buzz')

    def test_negative(self):
        self.assertEqual(fizzbuzz(-25), 'Buzz')
        self.assertEqual(fizzbuzz(-35), 'Buzz')
        self.assertEqual(fizzbuzz2(-45), 'FizzBuzz')
        self.assertEqual(fizzbuzz2(-55), 'Buzz')

    


if __name__ == '__main__':
    main()