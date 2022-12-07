package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type File struct {
	name string
	size int64
}

type Dir struct {
	name       string
	parent_dir *Dir
	files      []File
	dirs       []*Dir
}

func FindDirWithName(dirs []*Dir, name string) *Dir {
	for _, n := range dirs {
		if name == n.name {
			return n
		}
	}
	return nil
}

func create_dir_structure(input []string) *Dir {
	var current_dir, root_dir *Dir
	current_dir = &Dir{"/", nil, []File{}, []*Dir{}}
	root_dir = current_dir
	var ls_mode bool = false
	var lines []string = input[1:]
	for _, line := range lines {
		line = strings.TrimSpace(line)
		var line_tokens []string = strings.Split(line, " ")
		switch line_tokens[1] {
		case "cd":
			switch line_tokens[2] {
			case "..":
				current_dir = current_dir.parent_dir
			case "/":
				current_dir = root_dir
			default:
				current_dir = FindDirWithName(current_dir.dirs, line_tokens[2])
			}
			ls_mode = false
		case "ls":
			ls_mode = true
		default:
			if ls_mode {
				if line_tokens[0] == "dir" {
					current_dir.dirs = append(current_dir.dirs, &Dir{name: line_tokens[1], parent_dir: current_dir, files: []File{}, dirs: []*Dir{}})
				} else {
					fileSize, _ := strconv.ParseInt(line_tokens[0], 10, 0)
					current_dir.files = append(current_dir.files, File{line_tokens[1], fileSize})
				}
			}
		}
	}
	return root_dir

}

func get_dir_path_name(dir *Dir) string {
	current_dir := dir
	var path string = dir.name
	for current_dir.parent_dir != nil {
		path = current_dir.parent_dir.name + "/" + path
		current_dir = current_dir.parent_dir
	}
	return path
}

func get_dir_size(dir *Dir) int64 {
	var size int64 = 0
	for _, file := range dir.files {
		size += file.size
	}

	for _, dir := range dir.dirs {
		size += get_dir_size(dir)
	}
	return size
}

func get_dir_sizes(dir *Dir, dir_sizes map[string]int64) map[string]int64 {
	dir_sizes[get_dir_path_name(dir)] = get_dir_size(dir)
	for _, dir := range dir.dirs {
		dir_sizes = get_dir_sizes(dir, dir_sizes)
	}
	return dir_sizes
}

func part1(dir_sizes map[string]int64) int64 {
	var sum int64 = 0
	for _, size := range dir_sizes {
		if size <= 100000 {
			sum += size
		}
	}
	return sum
}

func part2(dir_sizes map[string]int64) int64 {
	total := dir_sizes["/"]
	sizes := make([]int64, 0, len(dir_sizes))
	for _, val := range dir_sizes {
		sizes = append(sizes, val)
	}
	sort.Slice(sizes, func(i, j int) bool { return sizes[i] < sizes[j] })

	for _, val := range sizes {
		if 70000000-(total-val) >= 30000000 {
			return val
		}
	}
	return total
}

func main() {
	filePath := "example_input.txt"
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	directory := create_dir_structure(fileLines)
	dir_sizes := get_dir_sizes(directory, make(map[string]int64))
	fmt.Println(part1(dir_sizes))
	fmt.Println(part2(dir_sizes))

}
