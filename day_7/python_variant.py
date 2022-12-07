from dataclasses import dataclass
from typing import List


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    name: str
    parent_dir: any  # Dir
    files: List[File]
    dirs: List[any]  # [Dir]


def create_dir_structure(input: List[str]):
    current_dir = Dir("/", None, [], [])
    root_dir = current_dir
    ls_mode = False
    lines = input[1:]
    for line in lines:
        line = line.strip()
        line = line.split()
        if (line[1] == "cd"):
            if line[2] == "..":
                current_dir = current_dir.parent_dir
            elif line[2] == "/":
                current_dir = root_dir
            else:
                current_dir = next(
                    x for x in current_dir.dirs if x.name == line[2])

            ls_mode = False
        elif (line[1] == "ls"):
            ls_mode = True
        elif ls_mode:
            if line[0] == "dir":
                current_dir.dirs.append(Dir(line[1], current_dir, [], []))
            else:
                current_dir.files.append(File(line[1], int(line[0])))
    return root_dir


def get_dir_size(dir):
    size = 0
    for file in dir.files:
        size += file.size
    for dir in dir.dirs:
        size += get_dir_size(dir)

    return size


def get_dir_path_name(dir):
    current_dir = dir
    path = dir.name
    while current_dir.parent_dir is not None:
        path = current_dir.parent_dir.name + "/" + path
        current_dir = current_dir.parent_dir
    return path


def get_dir_sizes(directory, dir_sizes={}):
    dir_sizes[get_dir_path_name(directory)] = get_dir_size(directory)
    for dir in directory.dirs:
        dir_sizes = get_dir_sizes(dir, dir_sizes)

    return dir_sizes


def part1(dir_sizes):
    sum = 0
    for dir_size in dir_sizes.values():
        if dir_size <= 100000:
            sum += dir_size
    return sum


def part2(dir_sizes):
    total = dir_sizes["/"]
    print(sorted(dir_sizes.values()))
    for dir_size in sorted(dir_sizes.values()):
        if 70000000 - (total - dir_size) >= 30000000:
            return dir_size


if __name__ == "__main__":
    with open('example_input.txt') as input_file:
        lines = input_file.readlines()
        directory = create_dir_structure(lines)
        dir_sizes = get_dir_sizes(directory)
        print(dir_sizes)
        print(part1(dir_sizes))
        print(part2(dir_sizes))
