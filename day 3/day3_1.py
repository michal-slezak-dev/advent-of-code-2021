def most_least_common(list, decision): # this function simply returns the most common bit, yes we could have used Counter etc.
    numOfOccurances = {element: list.count(element) for element in list} # count the number of occurances

    if decision: mostLeastCommonNum = max(numOfOccurances.values()) # get the min/max num of occurances depending on the decision argument
    else: mostLeastCommonNum = min(numOfOccurances.values())

    for bit in numOfOccurances:
        if numOfOccurances[bit] == mostLeastCommonNum:
            return bit # return the min/max num of occurances
    

with open("day_3.in") as puzzle_input:
    report = [line.strip() for line in puzzle_input]

numOfColumns = 12
columns = [[] for _ in range(numOfColumns)] # this list stores values from each column, each column has its own list, in which its bits are stored

for line in report:
    for i in range(numOfColumns):
        columns[i].append(line[i])

gamma_rate, epsilon_rate = "", ""
for column in columns:
    gamma_rate += most_least_common(column, True)
    epsilon_rate += most_least_common(column, False)

gamma_rate = int(gamma_rate, 2) # covert to decimal
epsilon_rate = int(epsilon_rate, 2) # covert to decimal

print(gamma_rate * epsilon_rate) # display 