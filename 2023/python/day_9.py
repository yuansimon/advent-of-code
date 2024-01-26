from util import *
from inputs.day_9 import input_1, input_2


def solve_1(input, debug=False):
    log = Logger(debug)
    next_values = []
    for line in parse_lines(input):
        nrs = [int(nr) for nr in line.split(" ")]
        log.print(nrs)
        i = 0
        all_nrs = dict()
        all_nrs[0] = nrs
        all_zeros = all(nr == 0 for nr in all_nrs[0])
        while not all_zeros:
            current_row = all_nrs[i]
            next_row = [current_row[j + 1] - current_row[j] for j in range(len(current_row) - 1)]
            all_nrs[i + 1] = next_row
            i += 1
            all_zeros = all(nr == 0 for nr in all_nrs[i])

        log.print("all nrs:", all_nrs)
        next_value = sum([all_nrs[j][-1] for j in range(i)])
        next_values.append(next_value)
    return sum(next_values)


def solve_2(input, debug=False):
    log = Logger(debug)
    previous_values = []
    for line in parse_lines(input):
        nrs = [int(nr) for nr in line.split(" ")]
        log.print(nrs)
        i = 0
        all_nrs = dict()
        all_nrs[0] = nrs
        all_zeros = all(nr == 0 for nr in all_nrs[0])
        while not all_zeros:
            current_row = all_nrs[i]
            next_row = [current_row[j + 1] - current_row[j] for j in range(len(current_row) - 1)]
            all_nrs[i + 1] = next_row
            i += 1
            all_zeros = all(nr == 0 for nr in all_nrs[i])

        log.print("all nrs:", all_nrs)
        first_values = [all_nrs[j][0] for j in range(i)]
        current = 0
        for j in range(i):
            k = i - j - 1
            current = first_values[k] - current
        log.print(current)
        previous_values.append(current)
    return sum(previous_values)


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
