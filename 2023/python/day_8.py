from util import *
from inputs.day_8 import input_1, input_2
import math


def solve_1(input, debug=False):
    log = Logger(debug)
    map = dict()
    directions = None
    for index, line in enumerate(parse_lines(input)):
        if index == 0:
            directions = line
            log.print("directions: ", directions)
            continue
        elif index == 1:
            assert line == ""
            continue

        parts = line.split("=")
        unparsed_map_values = parts[1][2:-1]
        left, right = unparsed_map_values.split(",")
        right = right.strip()
        key = parts[0].strip()
        log.print(f"{key}: ({left},{right})")
        map[key] = (left, right)

    current = "AAA"
    i = 0
    while True:
        direction = directions[i % len(directions)]
        assert direction in ["L", "R"]
        l, r = map[current]
        log.print(i, current, direction, l, r)
        if direction == "L":
            current = l
        else:
            current = r
        if current == "ZZZ":
            i += 1
            break
        i += 1
    return i


def solve_2(input, debug=False):
    log = Logger(debug)
    map = dict()
    directions = None
    for index, line in enumerate(parse_lines(input)):
        if index == 0:
            directions = line
            log.print("directions: ", directions)
            continue
        elif index == 1:
            assert line == ""
            continue

        parts = line.split("=")
        unparsed_map_values = parts[1][2:-1]
        left, right = unparsed_map_values.split(",")
        right = right.strip()
        key = parts[0].strip()
        log.print(f"{key}: ({left},{right})")
        map[key] = (left, right)

    starting_positions = [key for key in map.keys() if key[2] == "A"]
    steps = dict()
    log.print("starting positions", starting_positions)
    for starting_position in starting_positions:
        current = starting_position
        i = 0
        while True:
            direction = directions[i % len(directions)]
            assert direction in ["L", "R"]
            l, r = map[current]
            log.print(i, current, direction, l, r)
            if direction == "L":
                current = l
            else:
                current = r
            if current[2] == "Z":
                i += 1
                break
            i += 1
        steps[starting_position] = i
        log.print("Steps found: ", starting_position, i)

    current_lcm = None
    for step in steps.values():
        if current_lcm is None:
            current_lcm = step
        current_lcm = math.lcm(current_lcm, step)

    return current_lcm

def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
