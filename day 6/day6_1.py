with open("day_6.in") as puzzle_input:
    lantern_fish = puzzle_input.read().split(",")
    lantern_fish = [int(fish) for fish in lantern_fish] # get the input

for _ in range(80):
    for i in range(len(lantern_fish)):
        if lantern_fish[i] != 0: lantern_fish[i] -= 1 # each timer is substracted by 1  and added to the new dict
        else:
            lantern_fish[i] = 6 # rn, the timer of each (old) fish is being reset
            lantern_fish.append(8) # rn, we add a new timer of the currently created fish

print(len(lantern_fish))