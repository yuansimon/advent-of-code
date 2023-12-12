import unittest
from day_10 import solve_1, solve_2
import inputs.day_10 as real_data

input_1 = """.....
.S-7.
.|.|.
.L-J.
....."""
output_1 = 4

input_1b = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
output_1b = 8

input_2 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
output_2 = 4

input_2b = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""
output_2b = 4

input_2c = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
output_2c = 8

input_2d = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
output_2d = 10

input_2e = input_1
output_2e = 1


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(output_1, res)

    def test_solve_1b(self):
        res = solve_1(input_1b, debug=True)
        self.assertEqual(output_1b, res)

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(output_2, res)

    def test_solve_2b(self):
        res = solve_2(input_2b, debug=True)
        self.assertEqual(output_2b, res)

    def test_solve_2c(self):
        res = solve_2(input_2c, debug=True)
        self.assertEqual(output_2c, res)

    def test_solve_2d(self):
        res = solve_2(input_2d, debug=True)
        self.assertEqual(output_2d, res)

    def test_solve_2e(self):
        res = solve_2(input_2e, debug=True)
        self.assertEqual(output_2e, res)

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
