with open("day_7.in") as puzzle_input:
    crabs = puzzle_input.read().split(",") # get the input
    crabs = [int(crab) for crab in crabs]

fuel_cost = [[] for _ in range(min(crabs), max(crabs) + 1)] # it contains lists that store the fuel cost for each move from one position to anothe, for instance: 16 -> 2, 15 -> 1 etc.r
j = 0
for i in range(min(crabs), max(crabs) + 1): # check all of the possible positions
    for crab in crabs: # calculate the cost of their fuel used while moving to another position(min_position - min(crabs) | max_position - max(crabs))
        rightEnd = abs(crab - i) # right end of the interval
        # fuel_cost[j].append(sum([k for k in range(1, rightEnd + 1)])) # (slower) # the cost of their fuel = sum (start: 1, end: rightEnd) = 1 + 2 + ... + n | (n^2 + n) / 2
        fuel_cost[j].append((rightEnd ** 2 + rightEnd) / 2) # (faster) the cost of their fuel = sum (start: 1, end: rightEnd) = 1 + 2 + ... + n | (n^2 + n) / 2
    j += 1

fuel_cost_sums = [sum(listOfCosts) for listOfCosts in fuel_cost] # calculate the sum for each of the positions
print(min(int(fuel_cost_sums)))