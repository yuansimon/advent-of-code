import unittest
from day_5 import solve_1, solve_2, parse_translation, translate, translate_value_range
import inputs.day_5 as real_data

input_1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
output_1 = 35

input_2 = input_1
output_2 = 46


class MyTestCase(unittest.TestCase):
    def test_solve_1(self):
        res = solve_1(input_1, debug=True)
        self.assertEqual(output_1, res)

    def test_solve_2(self):
        res = solve_2(input_2, debug=True)
        self.assertEqual(output_2, res)

    def test_parse_translation(self):
        res = parse_translation("50 10 23")
        self.assertEqual(res, (10, 40, 23))
        res = parse_translation("20 50 11")
        self.assertEqual(res, (50, -30, 11))

    def test_translate(self):
        translations = [(10, 20, 3), (40, -10, 5)]
        test_data_set = [
            (2, 2),
            (10, 30),
            (12, 32),
            (13, 13),
            (39, 39),
            (40, 30),
            (44, 34),
            (45, 45),
        ]
        for test_data in test_data_set:
            res = translate(test_data[0], translations)
            self.assertEqual(res, test_data[1])

    def test_translate_value_range(self):
        translations = [(10, 20, 3), (20, -4, 5)]
        test_data_set = [
            ((2, 4), {(2, 4)}),
            ((2, 10), {(2, 9), (30, 30)}),
            ((2, 12), {(2, 9), (30, 32)}),
            ((2, 13), {(2, 9), (30, 32), (13, 13)}),
            ((2, 19), {(2, 9), (30, 32), (13, 19)}),
            ((2, 20), {(2, 9), (30, 32), (13, 19), (16, 16)}),
            ((2, 24), {(2, 9), (30, 32), (13, 19), (16, 20)}),
            ((2, 25), {(2, 9), (30, 32), (13, 19), (16, 20), (25, 25)}),
            ((11, 14), {(31, 32), (13, 14)}),
            ((20, 22), {(16, 18)}),
        ]
        for index, test_data in enumerate(test_data_set):
            res = translate_value_range(test_data[0], translations)
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
