
with open('input.txt') as input_file:
    elf_num = 0
    highest_calories = []
    current_calories = 0
    for line in input_file:
        if line == "\n":
            highest_calories.append(current_calories)
            current_calories = 0
        else:
            cal = int(line)
            current_calories += cal
    highest_calories.append(current_calories)
    highest_calories.sort(reverse=True)
    print(sum(highest_calories[:3]))
