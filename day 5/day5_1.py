with open("day_5.in") as puzzle_input:
    raw = [line.strip().split(" -> ") for line in puzzle_input] # split data "->" 

coordinates = [[] for _ in range(len(raw))] # this list contains the coordintates from each line of the puzzle_input
i = 0
for data in raw:
    for coords in data:
        commaIndex = coords.find(",")
        coordinates[i].append(int(coords[:commaIndex + 1].replace(",", ""))) # getting rid of commas -> int
        coordinates[i].append(int(coords[commaIndex:].replace(",", ""))) # getting rid of commas and converting -> int
    i += 1 # now the coordinates list comprises separated point [[x1, y1, x2, y2], ...] --> [[0, 9, 5, 9], ...]

all_lines = []
for points in coordinates: # points[0] -> x1 ; points[1] -> y1 ; points[2] -> x2 ; points[3] -> y2
    if points[0] != points[2] and points[1] != points[3]: continue # skip those points that are neither horizontal nor vertical
    else:
        floatPoint1, floatPoint2 = f"{str(points[0])}.{str(points[1])}", f"{str(points[2])}.{str(points[3])}" # get our initial points
        all_lines.append(floatPoint1)
        all_lines.append(floatPoint2)
    
        if points[0] == points[2] and points[1] < points[3]: # check if x1 = x2 and those points are like: 1,3 -> 1,5
            
            for i in range(points[1] + 1, points[3]):
                floatPoint = f"{str(points[0])}.{i}"
                all_lines.append(floatPoint)
                
        elif points[0] == points[2] and points[1] > points[3]: # check if x1 = x2 and those points are like: 2,2 -> 2,1
            
            for i in range(points[3] + 1, points[1]):
                floatPoint = f"{str(points[0])}.{i}"
                all_lines.append(floatPoint)
            
        elif points[1] == points[3] and points[0] < points[2]: # check if y1 = y1 and those points are like 0,9 -> 2,9        
            
            for i in range(points[0] + 1, points[2]):
                floatPoint = f"{str(i)}.{points[1]}"
                all_lines.append(floatPoint)
            
        elif points[1] == points[3] and points[0] > points[2]: # those points are like 9,7 -> 7,7
            
            for i in range(points[0] - 1, points[2], -1):
                floatPoint = f"{str(i)}.{points[1]}"
                all_lines.append(floatPoint)


num_of_occurances = {linePoint: all_lines.count(linePoint) for linePoint in all_lines} # count the numbers of occurances for each of the points
num_of_occurances = dict(filter(lambda val: val[1] >= 2, num_of_occurances.items())) # get rid of points that overlap less than 2

print(len(num_of_occurances)) # display the num of points that overlap