with open("day_2.in") as puzzle_input:
    commands = [[line.strip().split()[0], int(line.strip().split()[1])] for line in puzzle_input] # get the input

horizontal_pos, depth = 0, 0
for command in commands:
    command_txt = command[0] # example: 'forward'
    command_val = command[1] # example: '2'

    match command_txt:
        case "forward":
            horizontal_pos += command_val
        case "down":
            depth += command_val
        case _:
            depth -= command_val

print(f"Result: {horizontal_pos} * {depth} ==> {horizontal_pos * depth}")