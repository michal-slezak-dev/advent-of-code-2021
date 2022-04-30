from collections import defaultdict
with open("day_8.in") as puzzle_input:
    signals = [line.strip().split("|")[1].removeprefix(" ") for line in puzzle_input]

signals = [signal.split(" ") for signal in signals] 
numOfDivergentLetters = {2: 1, 4: 4, 3: 7, 7: 8} # set default keys for each [1, 4, 7, 8], a key is the length of the output value(num of unique letters) 

output_values = [output_val for signal in signals for output_val in signal] # add all of the values from each of the line
output_values = list(filter(lambda x: len(set(x)) in numOfDivergentLetters.keys(), output_values)) # delete values that aren't 1, 4, 7 or 8


numOfOccurances = defaultdict(int) # it contains the num of occurances for each seven-segment display
for output_val in output_values:
    numOfOccurances[numOfDivergentLetters[len(list(set(output_val)))]] += 1 # key = num of unique letters, whenever it seems the same, we increase the value by one
print(sum(numOfOccurances.values())) # we display the sum of those values
