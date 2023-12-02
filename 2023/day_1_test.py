import unittest
from day_1 import solve_1, solve_2, translate_digit

input_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

input_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(142, res)

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(281, res)

    def test_translate_digit(self):
        self.assertEqual("2", translate_digit("two"))
        self.assertEqual("2", translate_digit("owt"))
        self.assertEqual("2", translate_digit("2"))
        self.assertEqual("1", translate_digit("1"))


if __name__ == '__main__':
    unittest.main()
