from util import *
from inputs.day_5 import input_1, input_2


def parse_translation(line):
    parts = line.split(" ")
    assert len(parts) == 3
    destination = int(parts[0])
    source = int(parts[1])
    reach = int(parts[2])
    translation = destination - source
    return source, translation, reach


def parse_input(input, log=Logger(True)):
    maps = [None, None, None, None, None, None, None, None]
    first_lines = ["seeds",
                   "seed-to-soil",
                   "soil-to-fertilizer",
                   "fertilizer-to-water",
                   "water-to-light",
                   "light-to-temperature",
                   "temperature-to-humidity",
                   "humidity-to-location"]
    phase = 0
    for line in parse_lines(input):
        if maps[phase] is None:
            assert line.startswith(first_lines[phase])
            if phase == 0:
                unparsed_seeds = line.split(":")[1]
                maps[phase] = [int(seed) for seed in unparsed_seeds.split(" ") if seed != ""]
            else:
                maps[phase] = []
            continue

        if line == "":
            phase += 1
            continue

        assert 0 < phase < 8
        translation_tuple = parse_translation(line)
        maps[phase].append(translation_tuple)

    for index, map in enumerate(maps):
        if index > 0:
            map.sort()
    return maps


def translate(value, translation_tuples):
    for start, offset, reach in translation_tuples:
        if value < start:
            return value
        elif start <= value < start + reach:
            return value + offset
    return value


def translate_value_range(value_range, translation_tuples):
    final_value_ranges = set()
    v_start, v_end = value_range
    for t_start, offset, reach in translation_tuples:
        t_end = t_start + reach - 1
        if t_end < v_start:
            continue
        if v_end < t_start:
            final_value_ranges.add((v_start, v_end))
            v_start = v_end + 1
            break
        if v_start < t_start:
            final_value_ranges.add((v_start, t_start - 1))
            v_start = t_start
        if v_end <= t_end:
            final_value_ranges.add((v_start + offset, v_end + offset))
            v_start = v_end + 1
            break
        final_value_ranges.add((v_start + offset, t_end + offset))
        v_start = t_end + 1
    if v_start <= v_end:
        final_value_ranges.add((v_start, v_end))
    return final_value_ranges


def translate_value_ranges(value_ranges, translation_tuples, log=Logger(True)):
    final_value_ranges = set()
    for value_range in value_ranges:
        new_value_ranges = translate_value_range(value_range, translation_tuples)
        log.print(f"processing value_range {value_range} resulted in {new_value_ranges}")
        final_value_ranges |= new_value_ranges
    return final_value_ranges


def solve_1(input, debug=False):
    log = Logger(debug)
    maps = parse_input(input, log)
    seeds = maps[0]
    locations = []
    for seed in seeds:
        value = seed
        for phase in range(1, 8):
            value = translate(value, maps[phase])
        locations.append(value)
    return min(locations)


def solve_2(input, debug=False):
    log = Logger(debug)
    maps = parse_input(input, log)
    seeds = maps[0]
    assert len(seeds) % 2 == 0
    seed_ranges = [(seeds[i*2], seeds[i*2] + seeds[i*2 + 1] -1) for i in range(len(seeds) // 2)]
    log.print("seed ranges", seed_ranges)
    value_ranges = seed_ranges
    for phase in range(1, 8):
        log.print(f"value_ranges before processing phase {phase}: {value_ranges}")
        log.print(f"process using translation values: {maps[phase]}")
        value_ranges = translate_value_ranges(value_ranges, maps[phase], log=log)
    log.print(f"final value ranges {value_ranges}")
    value_ranges = list(value_ranges)
    value_ranges.sort()
    min_location_range = value_ranges[0]
    return min_location_range[0]


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
