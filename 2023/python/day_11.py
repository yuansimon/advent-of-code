from util import *
from inputs.day_11 import input_1, input_2

def calc_distances(input, expansion_factor=2, log=Logger(True)):
    lines = parse_lines(input)
    len_x = len(lines[0])

    empty_columns = set([x for x in range(len_x)])
    empty_rows = set()
    galaxies = []
    for y, line in enumerate(lines):
        if line == len_x * ".":
            empty_rows.add(y)
        else:
            for x, char in enumerate(line):
                if char == "#":
                    galaxies.append((x, y))
                    if x in empty_columns:
                        empty_columns.remove(x)
                    continue
                assert char == "."

    empty_rows = list(empty_rows)
    empty_rows.sort()
    empty_columns = list(empty_columns)
    empty_columns.sort()

    log.print(f"Found galaxies {galaxies} with empty rows {empty_rows} and empty columns: {empty_columns}")

    distances = 0
    for i in range(len(galaxies)):
        for j in range(i):
            g1_x, g1_y = galaxies[i]
            g2_x, g2_y = galaxies[j]

            x_values = [g1_x, g2_x]
            y_values = [g1_y, g2_y]
            x_values.sort()
            y_values.sort()

            empty_rows_between = sum([1 for row in empty_rows if y_values[0] < row < y_values[1]])
            empty_columns_between = sum([1 for col in empty_columns if x_values[0] < col < x_values[1]])

            expansion_x = empty_columns_between * (expansion_factor - 1)
            expansion_y = empty_rows_between * (expansion_factor - 1)

            distance_x = x_values[1] - x_values[0] + expansion_x
            distance_y = y_values[1] - y_values[0] + expansion_y
            distance = distance_x + distance_y
            distances += distance
            log.print(f"distance between {galaxies[i]} and {galaxies[j]} is {distance_x} + {distance_y} = {distance}")

    return distances


def solve_1(input, debug=False):
    log = Logger(debug)
    return calc_distances(input, expansion_factor=2, log=log)


def solve_2(input, debug=False):
    log = Logger(debug)
    return calc_distances(input, expansion_factor=1000000, log=log)


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
