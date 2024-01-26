import unittest
from day_7 import solve_1, solve_2
import inputs.day_7 as real_data

input_1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
output_1 = 6440

input_2 = input_1
output_2 = 5905


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(output_1, res)

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(output_2, res)

    # def test_(self):
    #     test_data_set = [
    #         (1,1),
    #     ]
    #     for index, test_data in enumerate(test_data_set):
    #         res = method(test_data[0])
    #         self.assertEqual(res, test_data[1])
    #         print(f"test {index} succeeded: {test_data}")


class TestCaseSolveReal(unittest.TestCase):
    def test_real_solve_1(self):
        res = solve_1(real_data.input_1)
        self.assertEqual(real_data.output_1, res)

    def test_real_solve_2(self):
        res = solve_2(real_data.input_2)
        self.assertEqual(real_data.output_2, res)


if __name__ == '__main__':
    unittest.main()
