def resize(array, size):
    if len(array) > size:
        return array[0:size]
    else:
        new_arr = [None for _ in range(size)]
        for i, item in enumerate(array):
            new_arr[i] = item
        return new_arr


def arr_appen(array, val):
    array = resize(array, len(array)+1)
    array[len(array)-1] = val
    return array


def arr_reverse(array):
    n = len(array)
    array = resize(array, n+1)
    for i in range(0, n // 2):
        array[n] = array[i]
        array[i] = array[n-i-1]
        array[n-i-1] = array[n]
    array = resize(array, n)
    return array


def stack_pop(stack):
    return stack[len(stack)-1], resize(stack, len(stack)-1),


def stack_push(stack, val):
    stack = resize(stack, len(stack)+1)
    stack[len(stack)-1] = val
    return stack


def parse_problem(input):
    lines = input.readlines()
    stacks = []
    num_container = 0
    rearr_proc = []
    part1 = True
    for line in lines:
        if part1 and line[0:2] != " 1":
            stacks.append(line)
        elif (line[0:2] == " 1"):
            num_container = int(line[-3])
            part1 = False
        else:
            rearr_proc.append(line)
    stacks = parse_stacks(stacks, num_container)
    rearr_proc = parse_rearr_proc(rearr_proc)
    return stacks, rearr_proc


def parse_stacks(stack_list, num_stack):
    stacks = [[] for _ in range(num_stack)]
    for stack_str in stack_list:
        for i in range(num_stack):
            if stack_str[1 + i * 4] != " ":
                stacks[i] = arr_appen(stacks[i], stack_str[1 + i * 4])
    for i, stack in enumerate(stacks):
        stacks[i] = arr_reverse(stack)
    return stacks


def parse_rearr_proc(rearr_proc):
    new_procs = []
    for proc in rearr_proc:
        proc_vals = [None for _ in range(3)]

        proc_toks = proc.split()
        if len(proc_toks) >= 6:
            # print(proc_toks, proc_toks[1], proc_toks[3], proc_toks[5][0])
            proc_vals[0] = int(proc_toks[1])
            proc_vals[1] = int(proc_toks[3])
            proc_vals[2] = int(proc_toks[5])
            new_procs.append(proc_vals)
            # print(new_procs)
    # print(new_procs)
    return new_procs


def move_between_stacks(num_to_move, from_stack_i, to_stack_i, stacks):
    from_stack = stacks[from_stack_i]
    to_stack = stacks[to_stack_i]
    # print(len(from_stack)-num_to_move, len(from_stack)-1)
    for i in range(num_to_move):
        popped_val, from_stack = stack_pop(from_stack)
        to_stack = stack_push(to_stack, popped_val)
    # from_stack = resize(from_stack, len(from_stack)-num_to_move)

    stacks[from_stack_i] = from_stack
    stacks[to_stack_i] = to_stack
    return stacks


def move_between_stacks(num_to_move, from_stack_i, to_stack_i, stacks):
    from_stack = stacks[from_stack_i]
    to_stack = stacks[to_stack_i]
    to_stack = resize(to_stack, len(to_stack)+num_to_move)
    for i in range(0, num_to_move):
        to_stack[len(to_stack)-num_to_move +
                 i] = from_stack[len(from_stack)-num_to_move+i]
    from_stack = resize(from_stack, len(from_stack)-num_to_move)

    # from_stack = resize(from_stack, len(from_stack)-num_to_move)

    stacks[from_stack_i] = from_stack
    stacks[to_stack_i] = to_stack
    # print(stacks)
    return stacks


if __name__ == "__main__":
    with open('example_input.txt') as input_file:
        stacks, rearr_proc = parse_problem(input_file)
        print(stacks, rearr_proc)
        for proc in rearr_proc:
            stacks = move_between_stacks(proc[0], proc[1]-1, proc[2]-1, stacks)
        print(stacks)
        out = ""
        for stack in stacks:
            out += stack[len(stack)-1]
        print(out)
