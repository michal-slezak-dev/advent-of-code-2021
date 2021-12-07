with open("day_7.in") as puzzle_input:
    crabs = puzzle_input.read().split(",") # get the input
    crabs = [int(crab) for crab in crabs]

fuel_cost = [[] for _ in range(min(crabs), max(crabs) + 1)] # it contains lists that store the fuel cost for each move from one position to another
j = 0
for i in range(min(crabs), max(crabs) + 1): # check all of the possible positions
    for crab in crabs: # calculate the cost of their fuel used while moving to another position(min_position - min(crabs) | max_position - max(crabs))
        fuel_cost[j].append(abs(crab - i))
    j += 1

fuel_cost_sums = [sum(listOfCosts) for listOfCosts in fuel_cost] # calculate the sum for each of the positions
print(min(fuel_cost_sums))