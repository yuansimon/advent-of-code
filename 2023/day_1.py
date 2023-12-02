from util import *
from inputs.day_1 import input_1, input_2


def solve_1(input, debug=False):
    digits_sum = 0
    first_digit = None
    last_digit = None
    input += "\n"
    for char in input:
        if char in digits:
            if first_digit is None:
                first_digit = char
            last_digit = char
        if char == "\n":
            assert first_digit
            num = int(first_digit + last_digit)
            if debug:
                print(num)
            digits_sum += num
            first_digit = None
            last_digit = None
    return digits_sum


def translate_digit(digit):
    if digit in digits:
        assert len(digit) == 1
        return digit
    for index, (digit_word, digit_word_rev) in enumerate(zip(digit_words, digit_words_rev)):
        if digit == digit_word or digit == digit_word_rev:
            return str(index + 1)
    assert False


def solve_2(input, debug=False):
    log = Logger(debug)
    digits_sum = 0
    lines = parse_lines(input)
    for line in lines:
        log.print("processing line", line)
        min_pos = len(line)
        first_digit = None
        last_digit = None
        for digit in digits_and_digits_words:
            pos = line.find(digit)
            if 0 <= pos < min_pos:
                min_pos = pos
                first_digit = digit

        line_rev = line[::-1]
        min_pos = len(line)
        for digit in digits_and_digits_words_rev:
            pos = line_rev.find(digit)
            if 0 <= pos < min_pos:
                min_pos = pos
                last_digit = digit

        log.print("first digit =", first_digit, ", last digit =", last_digit)
        num = int(translate_digit(first_digit) + translate_digit(last_digit))
        if debug:
            print(num)
        digits_sum += num
    return digits_sum


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
