with open("day1.in") as input:
    depths = [int(line.strip()) for line in input]

# calculate how many increases we can observe
depth_mesurment_increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        depth_mesurment_increases += 1
    else:
        continue

print(depth_mesurment_increases)