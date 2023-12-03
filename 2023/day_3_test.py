import unittest
from day_3 import solve_1, solve_2, parse_line

input_1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

input_1a = """.....
.*...
4.5.1
.#...
..300
.....
.*111
.....
22200
....*
.2000
.....
.9*..
.....
..20*"""

input_1b = """......
......
..99..
#.....
......
..10..
.#....
......
..11..
..#...
......
..12..
...#..
......
..13..
....#.
......
..14..
.....#"""

input_1c = """......
#.....
..99..
......
.#....
..10..
......
..#...
..11..
......
...#..
..12..
......
....#.
..13..
......
.....#
..14..
......"""

input_1d = """......
......
#.99..
......
.#10..
......
..11..
......
..12#.
......
..13.#
......"""

input_2 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(4361, res)

    def test_solve_1a(self):
        res = solve_1(input_1a, debug=True)
        self.assertEqual(24649, res)

    def test_solve_1b(self):
        res = solve_1(input_1b, debug=True)
        self.assertEqual(46, res)

    def test_solve_1c(self):
        res = solve_1(input_1c, debug=True)
        self.assertEqual(46, res)

    def test_solve_1d(self):
        res = solve_1(input_1d, debug=True)
        self.assertEqual(22, res)

    def test_parse_line(self):
        digits_dict = dict()
        symbols_dict = dict()

        line = "...*."
        line_nr = 0
        parse_line(line, line_nr, digits_dict, symbols_dict)
        self.assertEqual(digits_dict[line_nr], [])
        self.assertEqual(symbols_dict[line_nr], [3])

        line = ".2323"
        line_nr = 1
        parse_line(line, line_nr, digits_dict, symbols_dict)
        self.assertEqual(digits_dict[line_nr], [(1, "2323")])
        self.assertEqual(symbols_dict[line_nr], [])

        line = ".2*23"
        line_nr = 2
        parse_line(line, line_nr, digits_dict, symbols_dict)
        self.assertEqual(digits_dict[line_nr], [(1, "2"), (3, "23")])
        self.assertEqual(symbols_dict[line_nr], [2])

        line = "42.3."
        line_nr = 3
        parse_line(line, line_nr, digits_dict, symbols_dict)
        self.assertEqual(digits_dict[line_nr], [(0, "42"), (3, "3")])
        self.assertEqual(symbols_dict[line_nr], [])

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(467835, res)


if __name__ == '__main__':
    unittest.main()
