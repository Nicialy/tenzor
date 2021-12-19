from homework.dom4 import fib


class Testfibonachi:

    def test_fibonachi_10_55(self):
        assert fib(10) == 55

    def test_fib_minus_10_minus_1(self):
        assert fib(-10) == -1

    def test_fib_2_1(self):
        assert fib(2) == 1
