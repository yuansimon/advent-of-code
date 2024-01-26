from util import *
import math
from inputs.day_6 import input_1, input_2


def parse_input(input):
    lines = parse_lines(input)
    assert len(lines) == 2
    unparsed_times = lines[0].split(":")[1]
    unparsed_distances = lines[1].split(":")[1]
    times = [int(time) for time in unparsed_times.split(" ") if time != ""]
    distances = [int(distance) for distance in unparsed_distances.split(" ") if distance != ""]
    assert len(times) == len(distances)
    return [race for race in zip(times, distances)]


def num_wins(race, log=Logger(True)):
    t, r = race
    min_hold_time = int(math.floor((t - math.sqrt(t * t - 4 * r)) / 2)) + 1
    max_hold_time = int(math.ceil((t + math.sqrt(t * t - 4 * r)) / 2)) - 1
    log.print(f"min,max hold times for race {race}:", min_hold_time, max_hold_time)
    assert max_hold_time >= min_hold_time
    return max_hold_time - min_hold_time + 1


def solve_1(input, debug=False):
    log = Logger(debug)
    races = parse_input(input)
    log.print("races", races)
    product = 1
    for race in races:
        product *= num_wins(race, log)
    return product


def solve_2(input, debug=False):
    log = Logger(debug)
    races = parse_input(input)
    t_prefix = ""
    d_prefix = ""
    for race in races:
        t, d = race
        t_prefix += str(t)
        d_prefix += str(d)
    race = (int(t_prefix), int(d_prefix))
    log.print("race", race)
    return num_wins(race, log)


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
