def parse_input(str_array):
    lines = []
    for i, line in enumerate(str_array):
        line = line.strip().split()
        lines.append(line)
    return lines


def part1(file_name):
    lines = []
    with open(file_name) as input_file:
        lines = input_file.readlines()
        lines = parse_input(lines)

    register_X = 1
    curr_cycle = 1
    signal_strength_sum = 0
    for line in lines:
        cycle_inc = 0
        reg_X_inc = 0
        if line[0] == "noop":
            cycle_inc = 1
        elif line[0] == "addx":
            cycle_inc = 2
            reg_X_inc = int(line[1])
            # print(line[0], reg_X_inc)

        for _ in range(cycle_inc):
            # print("start", curr_cycle, register_X)
            if (curr_cycle - 20) % 40.0 == 0.0:
                print(curr_cycle, register_X, curr_cycle * register_X)
                signal_strength_sum += (curr_cycle * register_X)

            curr_cycle += 1
        register_X += reg_X_inc
        # print("endof", curr_cycle, register_X)

    print(signal_strength_sum)


def part2(file_name):
    lines = []
    with open(file_name) as input_file:
        lines = input_file.readlines()
        lines = parse_input(lines)

    register_X = 1
    curr_cycle = 1
    signal_strength_sum = 0
    crt_line = ""
    for line in lines:
        cycle_inc = 0
        reg_X_inc = 0
        if line[0] == "noop":
            cycle_inc = 1
        elif line[0] == "addx":
            cycle_inc = 2
            reg_X_inc = int(line[1])
            # print(line[0], reg_X_inc)

        for _ in range(cycle_inc):
            # print("start", curr_cycle, register_X)
            if (curr_cycle-1) % 40.0 == 0.0:
                print(crt_line)
                crt_line = ""
            sprite_pos = register_X
            pixel_pos = (curr_cycle % 40) - 1
            if pixel_pos <= sprite_pos + 1 and pixel_pos >= sprite_pos - 1:
                crt_line += "#"
            else:
                crt_line += "."
            curr_cycle += 1
        register_X += reg_X_inc
        # print("endof", curr_cycle, register_X)

    print(crt_line)
    print(signal_strength_sum)


if __name__ == "__main__":
    part2('input.txt')
