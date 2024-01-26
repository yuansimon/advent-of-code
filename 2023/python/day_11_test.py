import unittest
from day_11 import solve_1, solve_2, calc_distances
import inputs.day_11 as real_data

input_1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
output_1 = 374

input_2a = """##"""
input_2b = """#.#"""
input_2c = """#..#"""


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(output_1, res)

    def test_calc_distances(self):
        test_data_set = [
            (input_2a, 1, 1),
            (input_2a, 2, 1),
            (input_2a, 10, 1),
            (input_2b, 1, 2),
            (input_2b, 2, 3),
            (input_2b, 10, 11),
            (input_2c, 1, 3),
            (input_2c, 2, 5),
            (input_2c, 10, 21),
            (input_1, 2, output_1),
            (input_1, 10, 1030),
            (input_1, 100, 8410),
        ]
        for index, test_data in enumerate(test_data_set):
            res = calc_distances(test_data[0], test_data[1])
            self.assertEqual(res, test_data[2])
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
