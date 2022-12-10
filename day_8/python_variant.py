

def check_neighbours(y, x, input):
    curr_tree_val = input[y][x]

    left = [val for i, val in enumerate(input[y]) if i < x]
    right = [val for i, val in enumerate(input[y]) if i > x]
    top = [input[i][x] for i in range(len(input)) if i < y]
    bottom = [input[i][x] for i in range(len(input)) if i > y]
    return (max(left) < curr_tree_val) or (max(right) < curr_tree_val) or (max(top) < curr_tree_val) or (max(bottom) < curr_tree_val)


def get_score_in_direction(trees_in_direction, curr_tree):
    score = 0
    for height in trees_in_direction:
        if height >= curr_tree:
            score += 1
            break
        else:
            score += 1
    return score


def scenic_score(y, x, input):
    curr_tree_val = input[y][x]
    row_len = len(input[0])
    col_len = len(input)

    # from cell to edge
    left = [input[y][i] for i in range(row_len-1, -1, -1) if i < x]
    right = [input[y][i] for i in range(row_len) if i > x]
    top = [input[i][x] for i in range(col_len-1, -1, -1) if i < y]
    bottom = [input[i][x] for i in range(col_len) if i > y]

    left_score = get_score_in_direction(left, curr_tree_val)
    right_score = get_score_in_direction(right, curr_tree_val)
    top_score = get_score_in_direction(top, curr_tree_val)
    bottom_score = get_score_in_direction(bottom, curr_tree_val)
    return left_score * right_score * top_score * bottom_score


def main(file_name):
    with open(file_name) as input_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            lines[i] = line.strip()
            lines[i] = list(map(int, lines[i]))

    count = 0
    max_scenic_score = -1
    for y in range(1, len(lines)-1):
        for x in range(1, len(lines[0])-1):
            if check_neighbours(y, x, lines):
                count += 1
            max_scenic_score = max(max_scenic_score, scenic_score(y, x, lines))
    return (count + len(lines) * 2 + len(lines[0]) * 2 - 4), max_scenic_score


if __name__ == "__main__":
    part1, part2 = main('input.txt')
    print(part1, part2)
