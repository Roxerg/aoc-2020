with open('input13.txt', 'r') as file:
    goal, boops = file.readlines()
    goal = int(goal)
    
import numpy as np

# part 1
bops = boops.split(",")
bops = list(filter(lambda a: a != "x", bops))
bops = [int(bop) for bop in bops]
times = [bop for bop in bops]

best = goal*4
bbop = 0

for i in range(0,len(times)):
    while times[i] < goal:
        times[i] += bops[i]
    
    if times[i] < best:
        best = times[i]
        bbop = bops[i]


print((best-goal)*bbop)
print("-----")


# part 2

bops = boops.split(",")
diffs = []
i = 0
for bop in bops:
    if bop == "x":
        i +=1
    else:
        diffs.append(i)
        i += 1
bops = list(filter(lambda a: a != "x", bops))
bops = np.array([int(bop) for bop in bops])
times = np.array([bop for bop in bops])
diffs = np.array(diffs)


t, mult = 0,1
for i in range(0, len(times)):
    diff = diffs[i]
    bop  = bops[i]
    while (t+diff) % bop != 0:
        t += mult
    mult *= bop

print(t)
