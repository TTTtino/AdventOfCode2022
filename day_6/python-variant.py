def verify_if_marker(marker, marker_len):
    s = set()
    for char in marker:
        s.add(char)
    if (len(s)) != marker_len:
        return False
    return True


def detect_marker(input, marker_len):
    curr_marker = input[:marker_len]
    for i in range(marker_len, len(input)):
        print(curr_marker)
        if (verify_if_marker(curr_marker, marker_len)):
            return i
        else:
            curr_marker = curr_marker[1:]
            curr_marker += input[i]
    return -1


if __name__ == "__main__":
    with open('example_input.txt') as input_file:
        print(detect_marker(input_file.read(), 14))
