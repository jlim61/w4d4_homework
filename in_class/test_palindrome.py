from unittest import TestCase, main
from check_palindrome import check_palindrome

class TestCheckPalindrome(TestCase):

    def test_palindrome(self):
        self.assertTrue(check_palindrome('racecar'))
        self.assertTrue(check_palindrome('yobananaboy'))
        self.assertTrue(check_palindrome('poop'))

    def test_non_palindrome(self):
        self.assertFalse(check_palindrome('matrix'))
        self.assertFalse(check_palindrome('helloworld'))
        self.assertFalse(check_palindrome('sean'))
        self.assertEqual(check_palindrome('palindrome'), False)

    def test_casing(self):
        self.assertTrue(check_palindrome('Tacocat'))

    def test_uneven_amount_letters(self):
        self.assertTrue(check_palindrome('tacocat'))
        self.assertFalse(check_palindrome('boo'))

if __name__ == '__main__':
    main()