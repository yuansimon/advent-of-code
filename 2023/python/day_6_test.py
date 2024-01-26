import unittest
from day_6 import solve_1, solve_2, num_wins
import inputs.day_6 as real_data

input_1 = """Time:      7  15   30
Distance:  9  40  200"""
output_1 = 288

input_2 = input_1
output_2 = 71503


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(output_1, res)

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(output_2, res)

    def test_num_wins(self):
        test_data_set = [
            ((7, 9), 4),
            ((15, 40), 8),
            ((30, 200), 9),
        ]
        for index, test_data in enumerate(test_data_set):
            res = num_wins(test_data[0])
            self.assertEqual(res, test_data[1])
            print(f"test {index} succeeded: {test_data}")

class TestCaseSolveReal(unittest.TestCase):
    def test_real_solve_1(self):
        res = solve_1(real_data.input_1)
        self.assertEqual(real_data.output_1, res)

    def test_real_solve_2(self):
        res = solve_2(real_data.input_2)
        self.assertEqual(real_data.output_2, res)


if __name__ == '__main__':
    unittest.main()
