with open("day1_2.in") as input:
    depths = [int(line.strip()) for line in input]

# calculate all of the three-measurement sums
sums = []
for i in range(len(depths)):
    sums.append(sum(depths[i:i + 3]))

# calculate how many sums are larger than the previous ones
numOfSumsLargerThanThePreviousOne = 0
for i in range(1, len(sums)):
    if sums[i] > sums[i - 1]:
        numOfSumsLargerThanThePreviousOne += 1

print(numOfSumsLargerThanThePreviousOne)