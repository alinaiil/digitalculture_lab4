import unittest
import main as main_calc


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(main_calc.main(-1, 1, '+'), 0)

    def test_sub(self):
        self.assertEqual(main_calc.main(5, 5, '-'), 0)

    def test_mul(self):
        self.assertEqual(main_calc.main(2, 7, '*'), 14)

    def test_div(self):
        self.assertEqual(main_calc.main(8, 2, '/'), 4)


if __name__ == '__main__':
    unittest.main()
