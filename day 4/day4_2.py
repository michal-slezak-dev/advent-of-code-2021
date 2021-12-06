def check_if_row_or_col(board):
    row_count, col_count = 0, 0  
    for i in range(4, len(board), 5): # check rows
        if type(board[i - 4]) == type(board[i - 3]) == type(board[i - 2]) == type(board[i - 1]) == type(board[i]) == int:
            row_count += 5
        else:
            continue
    
    for i in range(len(board)): # check columns
        for j in range(i + 5, len(board), 5): # each column starts at +5
            if type(board[i]) == type(board[j]) == int:
                col_count += 1
        col_count = 0

    if row_count == 5 or col_count == 5:
        return True
    return False

def mark_nums(numsToBeDrawn, player_boards):
    calledNums = [] # it contains all of the calls made
    winning_boards = []
    for j in range(len(numsToBeDrawn)):
        for player_board in player_boards:
            for i in range(len(player_board)):
                if str(numsToBeDrawn[j]) == player_board[i] and type(player_board[i]) != int:
                    player_board[i] = int(numsToBeDrawn[j])
                    calledNums.append(numsToBeDrawn[j]) # the last element of this list is our last called num
            if check_if_row_or_col(player_board): # check if winner
                print(player_board)

def calculate_winning_score(winning_board):
    sum = 0
    for num in winning_board:
        if type(num) == str: sum += int(num)
    return sum

with open("day_4.in") as puzzle_input:
    input = [line.strip().split() for line in puzzle_input]  # get the entire puzzle_input
    numsToBeDrawn = input[0][0].split(",")  # get the first line with nums to be marked
    numsToBeDrawn = [int(num) for num in numsToBeDrawn]
    input.remove([])  # delete the 1st []
    input.remove(input[0])  # delete numsToBeDrawn from the boards list
    boards = input


boards = [line for line in boards if line != []]  # delete []
length  = len(boards) // 5
new_boards = [[] for _ in range(len(boards) // 5)] # number of boards

start = 0
five = 5
for i in range(length): 
    new_boards[i].extend(boards[start:five]) # line for each board
    start += 5
    five += 5

player_boards = [[] for _ in range(length)]
i = 0 
for new_board in new_boards: # merge each line(list) to the whole board
    for board in new_board:
        for element in board:
            player_boards[i].append(element)   
    i += 1

winning_board = mark_nums(numsToBeDrawn, player_boards) # winning board
print(mark_nums(numsToBeDrawn, player_boards))
print(calculate_winning_score(winning_board))