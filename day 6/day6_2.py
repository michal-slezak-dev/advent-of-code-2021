from collections import defaultdict

with open("day_6.in") as puzzle_input:
    fish_all = puzzle_input.read().split(",")
    lantern_fish = defaultdict(int)

    for fish in fish_all:
        lantern_fish[int(fish)] = fish_all.count(fish) # each timer has its own num of occurances

for _ in range(256):
    new_lantern = defaultdict(int) # temp dict containing new timers

    for timer in lantern_fish:
        if timer != 0: new_lantern[timer - 1] += lantern_fish[timer] # each timer is substracted by 1  and added to the new dict
        else:
            new_lantern[6] += lantern_fish[timer] # rn, the timer of each fish is being reset
            new_lantern[8] = lantern_fish[timer] # rn, we add a new timer of the currently created fish

    lantern_fish = new_lantern

print(sum(new_lantern.values()))