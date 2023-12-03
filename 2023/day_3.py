from util import *
from inputs.day_3 import input_1, input_2


def parse_line(line, line_nr, digits_dict, symbols_dict, gears_dict=dict(), log=Logger(True)):
    digit_prefix = ""
    digit_start = None
    if line_nr not in digits_dict:
        digits_dict[line_nr] = []
    if line_nr not in symbols_dict:
        symbols_dict[line_nr] = []
    if line_nr not in gears_dict:
        gears_dict[line_nr] = []

    for index, c in enumerate(line):
        if c in digits:
            if digit_prefix == "":
                digit_start = index
            digit_prefix += c
        else:
            if digit_start is not None:
                digits_dict[line_nr].append((digit_start, digit_prefix))
                digit_start = None
                digit_prefix = ""
            if c != ".":
                if c == "*":
                    gears_dict[line_nr].append(index)
                symbols_dict[line_nr].append(index)

    if digit_start is not None:
        digits_dict[line_nr].append((digit_start, digit_prefix))


def solve_1(input, debug=False):
    log = Logger(debug)

    digits_dict = dict()
    symbols_dict = dict()
    lines = parse_lines(input)
    for line_nr, line in enumerate(lines):
        log.print("parsing line:", line)
        parse_line(line, line_nr, digits_dict, symbols_dict, log=log)
        log.print("parsed digits_dict[line_nr] =", digits_dict[line_nr], ", symbols_dict[line_nr] = ",
                  symbols_dict[line_nr])

    nr_sum = 0
    for line_nr in range(len(lines)):
        line_nrs_to_check = [line_nr + i for i in range(-1, 2) if 0 <= line_nr + i < len(lines)]
        for digit_index, nr in digits_dict[line_nr]:
            log.print(f"checking line_nr={line_nr}, digit_index={digit_index}, nr={nr}")
            nr_checked = False
            for line_nr_to_check in line_nrs_to_check:
                for symbol in symbols_dict[line_nr_to_check]:
                    if digit_index -1 <= symbol <= digit_index + len(nr):
                        log.print(f"adding nr due to symbol at: ({line_nr_to_check},{symbol})")
                        nr_sum += int(nr)
                        nr_checked = True
                        break
                if nr_checked:
                    break

    return nr_sum


def solve_2(input, debug=False):
    log = Logger(debug)

    digits_dict = dict()
    symbols_dict = dict()
    gears_dict = dict()
    lines = parse_lines(input)
    for line_nr, line in enumerate(lines):
        log.print("parsing line:", line)
        parse_line(line, line_nr, digits_dict, symbols_dict, gears_dict, log=log)
        log.print("parsed digits_dict[line_nr] =", digits_dict[line_nr], ", gears[line_nr] = ",
                  gears_dict[line_nr])

    gear_ratio_sum = 0
    for line_nr in range(len(lines)):
        line_nrs_to_check = [line_nr + i for i in range(-1, 2) if 0 <= line_nr + i < len(lines)]
        for gear in gears_dict[line_nr]:
            digits_near_gear = []
            log.print(f"checking line_nr={line_nr}, gear={gear}")
            for line_nr_to_check in line_nrs_to_check:
                for digit_index, nr in digits_dict[line_nr_to_check]:
                    if digit_index - 1 <= gear <= digit_index + len(nr):
                        log.print(f"found digit ({line_nr_to_check}, {digit_index}, {nr}) for gear at ({line_nr},{gear})")
                        digits_near_gear.append(nr)
            if len(digits_near_gear) == 2:
                log.print("digits near gear:", digits_near_gear)
                gear_ratio = 1
                for nr in digits_near_gear:
                    gear_ratio *= int(nr)
                log.print("gear_ration", gear_ratio)
                gear_ratio_sum += gear_ratio

    return gear_ratio_sum


def main():
    print(solve_1(input_1,))
    print(solve_2(input_2,))


if __name__ == '__main__':
    main()
