with open("day_2.in") as puzzle_input:
    commands = [[line.strip().split()[0], int(line.strip().split()[1])] for line in puzzle_input] # get the input

horizontal_pos, depth, aim = 0, 0, 0

for command in commands:
    command_txt = command[0] # example: 'forward'
    command_val = command[1] # example: '2'

    # we can do it either using normal if statements or the newly added match case statement <3 
    match command_txt:
        case "down":
            aim += command_val
        case "up":
            aim -= command_val
        case _:
            horizontal_pos += command_val
            depth += aim * command_val

print(f"\nhorizontal position: {horizontal_pos}\ndepth: {depth}\naim: {aim}\nResult: horizontal_pos * depth ==> {horizontal_pos * depth}")