from time import time
from copy import deepcopy

with open('input15.txt', 'r') as file:
    g = [int(z) for z in file.readline().split(",")]


start = time()
# part 1
i = len(g)-1
f = deepcopy(g[::-1])
existset = set(f[1:])
print(existset)
print(f[1:])
while i < 2019:
    if f[0] in existset:
        dist = 1+f[1:].index(f[0])
        f.insert(0,dist)
    else:
        if f[0] != f[1]:
            f.insert(0,0)
        else:
            dist = 1+f[1:].index(f[0])
            f.insert(0,dist)

    existset.add(f[1])

    i += 1

end = time()
print(end-start)
print(f[0])

