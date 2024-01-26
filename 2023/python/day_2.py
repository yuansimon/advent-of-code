from util import *
from inputs.day_2 import input_1, input_2

colors = ["red", "green", "blue"]


def extract_rgb_color(rgb, unparsed_rgb):
    for unparsed_color in unparsed_rgb:
        for color in colors:
            if color in unparsed_color:
                rgb[color] = int(unparsed_color[:-len(color)])
                break
        else:
            assert False


def extract_rgb(unparsed_rgb):
    rgb = dict()
    extract_rgb_color(rgb, unparsed_rgb)
    for color in colors:
        if color not in rgb:
            rgb[color] = 0
    return rgb


def parse_line(line):
    game_prefix = line.split(":")[0]
    game_nr = int(game_prefix[len("Game"):])
    unparsed_games = line.split(":")[1]
    games = unparsed_games.split(";")
    unparsed_rgbs = [game.split(",") for game in games]
    rgb_list = [extract_rgb(unparsed_rgb) for unparsed_rgb in unparsed_rgbs]
    return game_nr, rgb_list


def solve_1(input, debug=False):
    log = Logger(debug)
    rgb_to_check = dict()
    rgb_to_check["red"] = 12
    rgb_to_check["green"] = 13
    rgb_to_check["blue"] = 14

    lines = parse_lines(input)
    game_nr_sum = 0
    for line in lines:
        log.print("processing line:", line)
        game_nr, rgb_list = parse_line(line)
        log.print("parsed game_nr =", game_nr, ", rgb_list = ", rgb_list)
        for rgb in rgb_list:
            if sum([int(rgb[color] <= rgb_to_check[color]) for color in colors]) != 3:
                break
        else:
            game_nr_sum += game_nr
    return game_nr_sum


def solve_2(input, debug=False):
    log = Logger(debug)
    lines = parse_lines(input)
    power_sum = 0
    for line in lines:
        log.print("processing line:", line)
        game_nr, rgb_list = parse_line(line)
        log.print("parsed game_nr =", game_nr, ", rgb_list = ", rgb_list)
        power = 1
        for color in colors:
            color_min_required = max([rgb[color] for rgb in rgb_list])
            log.print("color_min_required for color", color, "is", color_min_required)
            power *= color_min_required
        log.print("line power =", power)
        power_sum += power

    return power_sum


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
