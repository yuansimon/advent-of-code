import unittest
from day_1 import solve_1, solve_2, translate_digit
import inputs.day_1 as real_data

input_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
output_1 = 142

input_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
output_2 = 281


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(output_1, res)

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(output_2, res)

    def test_translate_digit(self):
        self.assertEqual("2", translate_digit("two"))
        self.assertEqual("2", translate_digit("owt"))
        self.assertEqual("2", translate_digit("2"))
        self.assertEqual("1", translate_digit("1"))


class TestCaseSolveReal(unittest.TestCase):
    def test_real_solve_1(self):
        res = solve_1(real_data.input_1)
        self.assertEqual(real_data.output_1, res)

    def test_real_solve_2(self):
        res = solve_2(real_data.input_2)
        self.assertEqual(real_data.output_2, res)


if __name__ == '__main__':
    unittest.main()
