from util import *
from inputs.day_10 import input_1, input_2
from queue import Queue


def get_neighbor_deltas_per_type(pipe_type):
    if pipe_type == "|":
        return {(0, -1), (0, +1)}
    elif pipe_type == "-":
        return {(-1, 0), (+1, 0)}
    elif pipe_type == "L":
        return {(0, -1), (+1, 0)}
    elif pipe_type == "J":
        return {(0, -1), (-1, 0)}
    elif pipe_type == "7":
        return {(0, 1), (-1, 0)}
    elif pipe_type == "F":
        return {(0, 1), (1, 0)}
    assert False


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
            if char == "S":
                start_pos = (x, y)
                continue
            if char == ".":
                continue

            deltas = get_neighbor_deltas_per_type(char)
            neighbors[(x, y)] = [(x + delta_x, y + delta_y) for delta_x, delta_y in deltas]

    log.print(f"Parsed Map. Starting Pos: {start_pos}. Map size: {x_len},{y_len}")
    return start_pos, x_len, y_len, neighbors, lines


def solve_1(input, debug=False):
    log = Logger(debug)
    start_pos, x_len, y_len, neighbors, lines = parse_map(input, log=log)
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
        loop_len, start_pos_pipe = path_to_start(start_connection, start_pos, neighbors, log=log)
        if loop_len != -1:
            log.print(f"found loop with len {loop_len} and start pipe type {start_pos_pipe}")
            assert loop_len % 2 == 0
            return loop_len // 2
    assert False


def path_to_start(search_pos, start_pos, neighbors, log=Logger(True), path_positions=set()):
    i = 1
    prev_pos = start_pos
    curr_pos = search_pos
    log.print(f"Follow pipe from {search_pos}")
    while True:
        if curr_pos not in neighbors:
            return -1, None
        curr_neighbors = neighbors[curr_pos]
        if curr_neighbors is None:
            return -1, None
        assert len(curr_neighbors) == 2
        path_positions.add(curr_pos)
        next_pos = [x for x in curr_neighbors if x != prev_pos]

        assert len(next_pos) == 1
        next_pos = next_pos[0]

        log.print(f"Curr: {curr_pos}, neighbors: {curr_neighbors}, next: {next_pos[0]}")

        i += 1
        if next_pos == start_pos:
            path_positions.add(start_pos)

            delta_1 = (search_pos[0] - start_pos[0], search_pos[1] - start_pos[1])
            delta_2 = (curr_pos[0] - start_pos[0], curr_pos[1] - start_pos[1])

            start_pos_pipe = [pipe for pipe in ["|", "-", "L", "J", "F", "7"] if
                              get_neighbor_deltas_per_type(pipe) == {delta_1, delta_2}]
            assert len(start_pos_pipe) == 1
            start_pos_pipe = start_pos_pipe[0]

            return i, start_pos_pipe
        prev_pos = curr_pos
        curr_pos = next_pos


def get_extended_map(path_positions, start_pos, lines, start_pos_pipe, log=Logger(True)):
    extended_map = set()

    log.print("Extending Map")
    for x, y in path_positions:
        if (x, y) == start_pos:
            pipe = start_pos_pipe
        else:
            pipe = lines[y][x]
        extended_x = x * 3
        extended_y = y * 3

        log.print(f"extend {pipe} at ({x},{y}) to ({extended_x, extended_y})")
        neighbors = [(extended_x + delta_x, extended_y + delta_y) for delta_x, delta_y in
                     get_neighbor_deltas_per_type(pipe)]

        extended_map.add((extended_x, extended_y))
        for neighbor in neighbors:
            log.print(f"extend {pipe} at ({x},{y}) to neighbor {neighbor}")
            extended_map.add(neighbor)

    return extended_map


def solve_2(input, debug=False):
    log = Logger(debug)
    start_pos, x_len, y_len, neighbors, lines = parse_map(input, log=log)
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
        path_positions = set()
        loop_len, start_pos_pipe = path_to_start(start_connection, start_pos, neighbors, path_positions=path_positions,
                                                 log=Logger(False))
        if loop_len != -1:
            log.print(f"found loop with len {loop_len} and start pipe type {start_pos_pipe}")
            break
    else:
        assert False

    extended_map = get_extended_map(path_positions, start_pos, lines, start_pos_pipe, log=Logger(False))

    print_extended_map(Logger(False), extended_map, x_len, y_len)
    visited = set(extended_map)

    exterior_points = flood_exterior((-1, -1), visited, x_len * 3, y_len * 3)
    log.print("Interior points:")
    print_extended_map(log, extended_map, x_len, y_len, exterior_points=exterior_points)

    interior_points_count = 0
    grid_3x3_deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    for x in range(x_len):
        for y in range(y_len):
            extended_x = x * 3
            extended_y = y * 3
            extended_3x3_grid_pos = [(extended_x + dx, extended_y + dy) for dx, dy in grid_3x3_deltas]
            if all([pos not in extended_map and pos not in exterior_points for pos in extended_3x3_grid_pos]):
                log.print(f"counting interior point ({x},{y})")
                interior_points_count += 1

    return interior_points_count


def flood_exterior(starting_pos, visited, x_len, y_len):
    exterior_points = set()
    queue = Queue()
    queue.put(starting_pos)
    neighbor_deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while not queue.empty():
        current_pos = queue.get()
        if current_pos in visited:
            continue
        exterior_points.add(current_pos)
        visited.add(current_pos)
        for delta_x, delta_y in neighbor_deltas:
            neighbor = (current_pos[0] + delta_x, current_pos[1] + delta_y)
            if neighbor not in visited and -1 <= neighbor[0] <= x_len and -1 <= neighbor[1] <= y_len:
                queue.put(neighbor)
    return exterior_points


def print_extended_map(log, extended_map, x_len, y_len, exterior_points=None):
    log.print(" ", end="")
    for x in range(x_len * 3):
        log.print(x % 10, end="")
    log.print()
    for y in range(y_len * 3):
        log.print(y % 10, end="")
        for x in range(x_len * 3):
            if (x, y) in extended_map:
                log.print("X", end="")
            elif exterior_points is not None and (x, y) not in exterior_points:
                log.print("I", end="")
            # elif exterior_points is not None and (x,y) in exterior_points:
            #     log.print("O", end="")
            else:
                log.print(".", end="")
        log.print()


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
