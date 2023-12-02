import unittest

digits = [str(x) for x in range(10)]
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_words_rev = [x[::-1] for x in digit_words]
digits_and_digits_words = digits + digit_words
digits_and_digits_words_rev = digits + digit_words_rev


def parse_lines(input):
    return input.split("\n")


class Logger:
    def __init__(self, debug):
        self.debug = debug

    def print(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)



input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


class MyTestCase(unittest.TestCase):
    def test_parse_lines(self):
        res = parse_lines(input)
        self.assertEqual(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], res)


if __name__ == '__main__':
    unittest.main()
