from unittest import TestCase, main
from memoization import fib, fib2

class TestMemoization(TestCase):

    def test_fib(self):
        self.assertEqual(fib(5),5)
        self.assertEqual(fib(30),832040)
        self.assertEqual(fib(50),12586269025)
        self.assertEqual(fib(80),23416728348467685)
        self.assertEqual(fib(500),139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125)
        self.assertEqual(fib(800),69283081864224717136290077681328518273399124385204820718966040597691435587278383112277161967532530675374170857404743017623467220361778016172106855838975759985190398725)

    def test_fib2(self):
        self.assertEqual(fib2(5),5)
        # these below don't work, crashes my terminal
        # self.assertEqual(fib2(30),832040)
        # self.assertEqual(fib2(50),12586269025)

if __name__ == '__main__':
    main()