import unittest
from day_X import solve_1, solve_2
import inputs.day_X as real_data

input_1 = """"""
output_1 = ""

input_2 = """"""
output_2 = ""


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
