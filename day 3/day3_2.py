def most_least_common(list, decision):  # this function simply returns the most/least common bit depending on our 'decision' boolean variable
    numOfOccurances = {element: list.count(element) for element in list}  # count the number of occurances

    if decision: mostLeastCommonNum = max(numOfOccurances.values())  # get the min/max num of occurances depending on the decision argument
    else: mostLeastCommonNum = min(numOfOccurances.values())

    bits = [bit for bit in numOfOccurances if numOfOccurances[bit] == mostLeastCommonNum] # append the bit even if there're two with the same numOfOccurances
    
    if len(bits) >= 2 and decision: return '1'  # return '1' if the number of occurances is the same for both '0' and '1' and it's oxygen
    elif len(bits) >= 2 and not decision: return '0' # return '0' if the bnumber of occurances is the same for both '0' and '1' and it's co2
    else: return bits[0] # return '0' or '1' if there's only one that is the most common

def delete_if_invalid(key, list, index): # delete elements that doesn not contain the key ex.: '1'
    new_list = [element for element in list if element[index] == key] 

    return new_list

def get_columns(list, num):
    columns = [[]]  # this list stores values from the num-th column

    for line in list:
        columns[0].append(line[num])

    return columns

def find_oxygen_generator_rating(report):
    columns = get_columns(report, 0)  # generate the first bit column
    currentMostCommonBit = most_least_common(columns[0], True) # get the most common bit
    report = delete_if_invalid(currentMostCommonBit, report, 0)  # after 1st filtration, we can use filter() as well, but if we wanna do so, we should change our function a bit

    j = 1
    for i in range(len(report)):
        columns = get_columns(report, j)  # create a new 'column' for the j-th bit
        currentMostCommonBit = most_least_common(columns[0], True)  # find the most common bit
        report = delete_if_invalid(currentMostCommonBit, report, j)  # delete binary string that doesn not contain this bit on their j-th position

        if len(report) == 1:
            break
        j += 1
    return report[0]

def find_co2_scrubber_rating(report):
    columns = get_columns(report, 0)  # generate the first bit column
    currentLeastCommonBit = most_least_common(columns[0], False) # get the least common beat
    report = delete_if_invalid(currentLeastCommonBit, report, 0)  # after 1st filtration, we can use filter() as well, but if we wanna do so, we should change our function a bit

    j = 1
    for i in range(len(report)):
        columns = get_columns(report, j)  # create a new 'column' for the j-th bit
        currentLeastCommonBit = most_least_common(columns[0], False)  # find the most common bit
        report = delete_if_invalid(currentLeastCommonBit, report, j)  # delete binary string that doesn not contain this bit on their j-th position

        if len(report) == 1:
            break
        j += 1
    return report[0]

with open("day_3.in") as puzzle_input:
    report = [line.strip() for line in puzzle_input] # get the input

oxygenGeneratorRating = int(find_oxygen_generator_rating(report), 2) # convert to decimal
co2ScrubberRating = int(find_co2_scrubber_rating(report), 2) # conver to decimal

print(f"{oxygenGeneratorRating} * {co2ScrubberRating} ==> {oxygenGeneratorRating * co2ScrubberRating}") # display the result