from util import *
from inputs.day_10 import input_1, input_2


def parse_map(input, log=Logger(True)):
    x_len = None
    start_pos = None

    lines = parse_lines(input)
    y_len = len(lines)
    neighbors = dict()
    for y, line in enumerate(lines):
        if x_len is None:
            x_len = len(line)
        else:
            assert x_len == len(line)
        for x, char in enumerate(line):
            if char == "|":
                neighbors[(x, y)] = [(x, y - 1), (x, y + 1)]
            elif char == "-":
                neighbors[(x, y)] = [(x - 1, y), (x + 1, y)]
            elif char == "L":
                neighbors[(x, y)] = [(x, y - 1), (x + 1, y)]
            elif char == "J":
                neighbors[(x, y)] = [(x, y - 1), (x - 1, y)]
            elif char == "7":
                neighbors[(x, y)] = [(x, y + 1), (x - 1, y)]
            elif char == "F":
                neighbors[(x, y)] = [(x, y + 1), (x + 1, y)]
            elif char == "S":
                start_pos = (x, y)
            else:
                assert char == "."
    log.print(f"Starting Pos: {start_pos}. Map size: {x_len},{y_len}")
    return start_pos, x_len, y_len, neighbors


def solve_1(input, debug=False):
    log = Logger(debug)
    start_pos, x_len, y_len, neighbors = parse_map(input, log=log)
    start_x, start_y = start_pos
    start_connections = [
        (start_x + 1, start_y),
        (start_x - 1, start_y),
        (start_x, start_y + 1),
        (start_x, start_y - 1)
    ]
    start_connections = [pos for pos in start_connections if pos in neighbors and start_pos in neighbors[pos]]
    log.print("start connections", start_connections)

    for start_connection in start_connections:
        loop_len = path_to_start(start_connection, start_pos, neighbors,log=log)
        if loop_len != -1:
            log.print("found loop len:", loop_len)
            assert loop_len % 2 == 0
            return loop_len // 2
    assert False


def path_to_start(search_pos, start_pos, neighbors, log=Logger(True)):
    i = 1
    prev_pos = start_pos
    curr_pos = search_pos
    while True:
        if curr_pos not in neighbors:
            return -1
        curr_neighbors = neighbors[curr_pos]
        if curr_neighbors is None:
            return -1
        assert len(curr_neighbors) == 2
        next_pos = [x for x in curr_neighbors if x != prev_pos]

        log.print(curr_pos, curr_neighbors, next_pos[0])

        assert len(next_pos) == 1
        next_pos = next_pos[0]

        i += 1
        if next_pos == start_pos:
            return i
        prev_pos = curr_pos
        curr_pos = next_pos


def solve_2(input, debug=False):
    log = Logger(debug)
    for line in parse_lines(input):
        pass


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
