def parse_input(str_array):
    lines = []
    for i, line in enumerate(str_array):
        line = line.strip().split()
        lines.append((line[0], int(line[1])))
    return lines


def move_head(h_pos, move_dir):
    x, y = h_pos
    if move_dir == 'U':
        return (x, y+1)
    elif move_dir == 'D':
        return (x, y-1)
    elif move_dir == 'L':
        return (x-1, y)
    elif move_dir == 'R':
        return (x+1, y)

    return h_pos


def move_tail(t_pos, h_pos):
    t_x, t_y = t_pos
    h_x, h_y = h_pos

    if (t_x <= h_x + 1 and t_x >= h_x - 1 and t_y <= h_y + 1 and t_y >= h_y - 1) or (t_x == h_x and t_y == h_y):
        return t_pos

    if h_x > t_x:
        t_x += 1
    if h_x < t_x:
        t_x -= 1
    if h_y > t_y:
        t_y += 1
    if h_y < t_y:
        t_y -= 1

    return (t_x, t_y)


def part1(file_name):
    lines = []
    with open(file_name) as input_file:
        lines = input_file.readlines()
        lines = parse_input(lines)
    visited = set()
    h_pos = (0, 0)
    t_pos = (0, 0)

    for inp in lines:
        for _ in range(inp[1]):
            h_pos = move_head(h_pos, inp[0])
            t_pos = move_tail(t_pos, h_pos)
            visited.add(t_pos)

    print(h_pos, t_pos, len(visited))


def part2(file_name):
    lines = []
    with open(file_name) as input_file:
        lines = input_file.readlines()
        lines = parse_input(lines)
    visited = set()
    h_pos = (0, 0)
    t_poss = [(0, 0) for _ in range(9)]

    for inp in lines:
        for _ in range(inp[1]):
            h_pos = move_head(h_pos, inp[0])
            curr_pos = h_pos
            for i, t_pos in enumerate(t_poss):
                t_poss[i] = move_tail(t_pos, curr_pos)
                curr_pos = t_poss[i]
            visited.add(t_poss[8])

    print(h_pos, t_pos, len(visited))
    return len(visited)


if __name__ == "__main__":
    part2('input.txt')
